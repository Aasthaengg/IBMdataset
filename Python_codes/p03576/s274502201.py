N, K = [int(_) for _ in input().split()]

P = [[int(_) for _ in input().split()] for n in range(N)]

X = []
Y = []
for n in range(N):
    x, y = P[n]
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

ans = 10 ** 20
for xi in range(N):
    for xj in range(xi+1, N):
        for yi in range(N):
            for yj in range(yi+1, N):
                x1, y1 = X[xi], Y[yi]
                x2, y2 = X[xj], Y[yj]
                c = 0
                for v in range(N):
                    x, y = P[v]
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        c += 1
                if c >= K:
                    ans = min(ans, (x2-x1) * (y2-y1))
print(ans)
