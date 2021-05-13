x, y = map(int, input().split())

l = [4, 6, 9, 11]

if x == 2 or y == 2:
    print('No')
elif (l.count(x) > 0 and l.count(y) == 0) or (l.count(x) == 0 and l.count(y) > 0):
    print('No')
else:
    print('Yes')
