n = int(input())
now, nx, ny = [0, 0, 0]

f = True
for i in range(n):
    t, x, y = map(int, input().split())
    mdist = abs(nx-x) + abs(ny-y)
    if t - now < mdist:
        f = False
        break
    elif mdist%2 != (t-now)%2:
        f = False
        break
    else:
        now = t
        nx, ny = x, y
if f:
    print('Yes')
else:
    print('No')
