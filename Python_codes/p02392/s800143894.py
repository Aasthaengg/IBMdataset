arr = input().split(' ')
(a, b, c) = tuple([int(x) for x in arr])

if (a < b < c):
    print('Yes')
else:
    print('No')