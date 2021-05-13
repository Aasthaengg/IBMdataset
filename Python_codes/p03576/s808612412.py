n,k = map(int,input().split())
x = []
y = []
xx = []
yy = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
    xx.append(a)
    yy.append(b)
ans = 10 ** 40
x.sort()
y.sort()
for i in range(n):
    for j in range(i+1,n):
        for l in range(n):
            for h in range(l+1,n):
                lx = x[i]
                rx = x[j]
                uy = y[h]
                dy = y[l]
                cnt = 0
                for ii in range(n):
                    if lx <= xx[ii] <= rx and dy <= yy[ii] <= uy:
                        cnt += 1
                if cnt >= k:
                    if (rx-lx) * (uy-dy) != 0:
                        ans = min(ans,(rx-lx)*(uy-dy))
print(ans)