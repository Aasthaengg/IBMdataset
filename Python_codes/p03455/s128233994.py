INPUT = list(map(int,input().split()))

a = INPUT[0]
b = INPUT[1]

if a * b % 2:
    print('Odd')
else:
    print('Even')