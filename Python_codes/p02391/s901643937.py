(a, b) = input().rstrip().split(' ')
a = int(a)
b = int(b)

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')