x, y = map(int, input().split())
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
if a.count(x) != 0 and a.count(y) != 0:
    print('Yes')
elif b.count(x) != 0 and b.count(y) != 0:
    print('Yes')
elif c.count(x) != 0 and c.count(y) != 0:
    print('Yes')
else:
    print('No')