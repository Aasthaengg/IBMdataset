n, k = map(int, input().split())
xv, yv = [], []
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xv.append(x)
    yv.append(y)
    xy.append((x, y))

xv = sorted(xv)
yv = sorted(yv)
ans = (xv[n-1] - xv[0]) * (yv[n-1] - yv[0])
for l in range(n):
    lx = xv[l]
    for r in range(l+1, n):
        rx = xv[r]
        for b in range(n):
            by = yv[b]
            for t in range(b+1, n):
                ty = yv[t]
                cnt = 0
                for x, y in xy:
                    if lx <= x <= rx and by <= y <= ty:
                        cnt += 1
                if cnt >= k:
                    ans = min(ans, (rx - lx)*(ty - by))
print(ans)
