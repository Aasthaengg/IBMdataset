N = int(input())
dt, dx, dy = 0, 0, 0
avilable = True
for i in range(N):
    t, x, y = map(int, input().split())
    if abs(x-dx)+abs(y-dy) > t-dt or (abs(x-dx)+abs(y-dy)) % 2 != (t-dt) % 2:
        avilable = False
    dt = t
    dx = x
    dy = y
if avilable:
    print('Yes')
else:
    print('No')
