N, C = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

Y = [[C - i, v] for i, v in X[::-1]]

# Cumsum
x_cs = [[0, 0] for _ in range(N + 1)]
y_cs = [[0, 0] for _ in range(N + 1)]
for i in range(N):
    x_cs[i + 1][0] = X[i][0]
    x_cs[i + 1][1] = x_cs[i][1] + X[i][1]

    y_cs[i + 1][0] = Y[i][0]
    y_cs[i + 1][1] = y_cs[i][1] + Y[i][1]

fx = [v - x for x, v in x_cs]
fy = [v - x for x, v in y_cs]

gx = [0] * (N + 1)
gy = [0] * (N + 1)
for i in range(N):
    gx[i + 1] = max(gx[i], fx[i + 1])
    gy[i + 1] = max(gy[i], fy[i + 1])

X = [[0, 0]] + X
Y = [[0, 0]] + Y
ans = max(gx + gy)
for i in range(N + 1):
    ans = max(ans, gx[i] + gy[N - i] - X[i][0],
              gx[N - i] + gy[i] - Y[i][0])

print(ans)
