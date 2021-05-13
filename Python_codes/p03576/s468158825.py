N, K = map(int, input().split())
XY = sorted([tuple(map(int, input().split())) for _ in range(N)])

ans = 10 ** 20
for xl in range(N):
    for xr in range(xl + 1, N):
        Ysub = sorted([y for x, y in XY[xl:xr + 1]])
        for i in range(xr - xl - K + 2):
            Yk = Ysub[i:i + K] + [XY[xr][1], XY[xl][1]]
            ans = min(ans, (XY[xr][0] - XY[xl][0]) * (max(Yk) - min(Yk)))

print(ans)
