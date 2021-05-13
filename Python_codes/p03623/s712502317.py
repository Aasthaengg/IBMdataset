x, a, b = map(int,input().split())
ax = abs(a-x)
bx = abs(b-x)
if ax < bx:
    print('A')
else:
    print('B')