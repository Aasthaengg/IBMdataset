arr = input().split(' ')
(a, b) = tuple([int(x) for x in arr])

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')