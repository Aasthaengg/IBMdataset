def cnt(xl, xr, yb, yt):
    c = 0
    for i in range(n):
        if xl <= xy[i][0] <= xr and yb <= xy[i][1] <= yt:
            c += 1
    return c


n, k = map(int, input().split())

x = []
y = []
xy = []
for i in range(n):
    u, v = map(int, input().split())
    x.append(u)
    y.append(v)
    xy.append([u,v])
    
x.sort()
y.sort()

ans = (x[-1]-x[0])*(y[-1]-y[0])
for l in range(n-1):
    for r in range(l+1, n):
        xl, xr = x[l], x[r]
        for b in range(n-1):
            for t in range(b+1, n):
                yb, yt = y[b], y[t]
                s = (xr-xl)*(yt-yb)
                if s < ans:
                    ck = cnt(xl, xr, yb, yt)
                    # print(xl, xr, yb, yt, ck)
                    if ck >= k:
                        ans = s
print(ans)
