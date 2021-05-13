n = int(input())
As = [list(map(int, input().split())) for _ in range(n)]

import copy
d = copy.deepcopy(As)
for i in range(n):
    for k in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
cnt = 0
routes = set()
for i in range(n):
    for j in range(i+1,n):
        routes.add(i*n+j)


for i in range(n):
    for k in range(n):
        for j in range(n):
            x = (i-j)*(j-k)*(k-i)
            # かぶりを消す
            if d[i][j] == d[i][k]+d[k][j] and x != 0:
                try:
                    routes.remove(i*n+j)
                except:
                    pass
cnt = 0
for r in routes:
    i,j = divmod(r,n)
    cnt += d[i][j]

if As != d:
    print(-1)
else:
    print(cnt)