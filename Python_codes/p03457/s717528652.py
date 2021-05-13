#!/user/bin/env python3

n = int(input())
t = [-1 for _ in range(n)]
x = [-1 for _ in range(n)]
y = [-1 for _ in range(n)]
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())

dt = [-1 for _ in range(n)]
dx = [-1 for _ in range(n)]
dy = [-1 for _ in range(n)]
for i in range(n):
    if i == 0:
        dt[0] = t[0]
        dx[0] = x[0]
        dy[0] = y[0]
    else:
        dt[i] = t[i] - t[i-1]
        dx[i] = x[i] - x[i-1]
        dy[i] = y[i] - y[i-1]

ok = True
for i in range(n):
    tr = dt[i]%2
    pr = (dx[i]+dy[i])%2
    if (tr == pr) and (dt[i] >= abs(dx[i])+abs(dy[i])):
        pass
    else:
        ok = False
#        import pdb; pdb.set_trace()
        break

if ok:
    print('Yes')
else:
    print('No')