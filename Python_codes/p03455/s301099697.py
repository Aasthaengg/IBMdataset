input = input().strip().split()
a = int(input[0])
b = int(input[1])

if a % 2 == 0 or b % 2 == 0:
    print('Even')
else:
    print('Odd')
