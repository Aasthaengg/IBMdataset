N, W = map(int, input().split())
I = [tuple(map(int, input().split())) for _ in range(N)]
w0 = I[0][0]

dp = [[[0 for k in range(N * 3 + 1)] for j in range(N + 1)] for i in range(N + 1)]

for i in range(N):
    w, v = I[i]
    for j in range(N):
        for k in range(3 * N + 1):
            if k - (w - w0) >= 0:
                dp[i + 1][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k - (w - w0)] + v)
            else:
                dp[i + 1][j + 1][k] = dp[i][j + 1][k]

res = 0

for i in range(N + 1):
    for j in range(N + 1):
        for k in range(3 * N + 1):
            if w0 * j + k <= W:
                res = max(res, dp[i][j][k])

print(res)