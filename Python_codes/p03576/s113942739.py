n, k = map(int, input().split())
XY = []
xs = []
ys = []
for i in range(n):
    x, y = map(int, input().split())
    XY.append((x, y))
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()
ans = float('inf')
for a in range(n-1):
    for b in range(a+1, n):
        for c in range(n-1):
            for d in range(c+1, n):
                xl = xs[a]
                xr = xs[b]
                yl = ys[c]
                yu = ys[d]
                cnt = 0
                for x, y in XY:
                    if xl <= x <= xr and yl <= y <= yu:
                        cnt += 1
                if cnt >= k:
                    ans = min(ans, (xr-xl)*(yu-yl))
print(ans)
