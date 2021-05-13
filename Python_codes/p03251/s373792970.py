n, m, xx, yy = map(int, input().split())
x = list(map(int , input().split()))
y = list(map(int , input().split()))
x.sort()
y.sort()

zx = max(x[-1], xx)
zy = min(y[0], yy)

if yy == x[-1]:
    print('War')
    exit()
if xx == y[0]:
    print('War')
    exit()
if x[-1] == y[0]:
    print('War')
    exit()
if zx > zy:
    print('War')
    exit()

print('No War')