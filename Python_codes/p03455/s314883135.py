input_list = input().split(' ')
a = int(input_list[0])
b = int(input_list[1])

N = a*b

if N%2==0:
    print('Even')
else:
    print('Odd')

del input_list