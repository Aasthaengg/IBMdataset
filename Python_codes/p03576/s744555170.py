from copy import deepcopy
N, K = map(int, input().split())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
PX, PY = deepcopy(X), deepcopy(Y)
X.sort()
Y.sort()

ans = (X[-1] - X[0]) * (Y[-1] - Y[0])

for xi in range(N - 1):
    for xj in range(xi + 1, N):
        for yi in range(N - 1):
            for yj in range(yi + 1, N):
                num = 0
                lx, rx = X[xi], X[xj]
                by, uy = Y[yi], Y[yj]

                for i in range(N):
                    if lx <= PX[i] and PX[i] <= rx and by <= PY[i] and PY[i] <= uy:
                        num += 1

                if num >= K:
                    ans = min(ans, (rx - lx) * (uy - by))
print(ans)
