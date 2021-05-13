n, k = map(int, input().split())
point = []
xarray = []
yarray = []
for _ in range(n):
    x, y = map(int, input().split())
    point.append([x, y])
    xarray.append(x)
    yarray.append(y)

xarray.sort()
yarray.sort()

ans = 4*(10**18)+10
for xi in range(n):
    for xj in range(xi+1, n):
        for yi in range(n):
            for yj in range(yi+1, n):
                lx, rx = xarray[xi], xarray[xj]
                by, ay = yarray[yi], yarray[yj]
                num = 0
                for i in range(n):
                    x, y = point[i]
                    if lx <= x <= rx and by <= y <= ay:
                        num += 1
                if num >= k:
                    ans = min(ans, (rx-lx)*(ay-by))
print(ans)