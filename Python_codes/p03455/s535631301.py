data = input()

num1,num2 = data.split(' ')

num1 = int(num1)
num2 = int(num2)

number = (num1 * num2) % 2

if number == 0:
    print('Even')
else:
    print('Odd')