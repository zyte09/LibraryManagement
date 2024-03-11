import sys
listbook = ['Lookism', 'Solo leveling', 'Weak hero', 'Get schooled', 'Build up', 'No scope', 'Wind breaker']
print('\n       Welcome to the book rental system \n------------------------------------------------')
def library():
    while True:
        print('Enter 1. To display available books \nEnter 2. To borrow a book \nEnter 3. To return a book \nEnter 4. To exit')
        choice = input('Select a choice from 1-4: ')
        if int(choice) == 1:
            print('\nThe available books right now are: ')
            for i in range(len(listbook)):
                print(' '+listbook[i])
            continue
        elif int(choice) == 2:
            bookchoice = input('Enter the name of the book you want to borrow: ')
            if bookchoice in listbook:
                print("You have borrowed the " + bookchoice + " book. Please return it within 14 days")
                listbook.remove(bookchoice)
            else:
                print("Sorry, This book is unavailable. Please borrow another book that is available")
            print('\n       Welcome to the book rental system \n------------------------------------------------')
            continue

        elif int(choice) == 3:
            bookreturn = input('What book would you like to return: ')
            listbook.append(bookreturn)
            print('Thank you for returning this book')
            print('\n       Welcome to the book rental system \n------------------------------------------------')
            continue

        elif int(choice) == 4:
            print('Thank you for using the book rental system. Have a great day!')
            sys.exit()
while True:
    try:
        library()
    except ValueError:
        print('Invalid Input. Please try again')