input_list = input().split()

a = int(input_list[0])
b = int(input_list[1])

if a * b % 2 == 0:
    print('Even')
else:
    print('Odd')