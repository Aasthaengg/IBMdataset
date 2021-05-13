n = int(input())
TA = [list(map(int, input().split())) for _ in range(n)]

XY = [TA[0]]

for i in range(1, n):
    x0, y0 = XY[i-1]
    x1, y1 = TA[i]
    xq, xr = divmod(x0, x1)
    yq, yr = divmod(y0, y1)
    if xr != 0:
        xq += 1
    if yr != 0:
        yq += 1
    q = max(xq, yq)
    x1, y1 = x1*q, y1*q
    XY.append([x1, y1])
    
print(sum(XY[-1]))