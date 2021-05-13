N, X, Y = [int(_) for _ in input().split()]

INF = 10 ** 9
dp = [[INF] * N for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        dp[i][j] = j - i
        dp[j][i] = j - i

dp[X - 1][Y - 1] = 1
dp[Y - 1][X - 1] = 1

for k in [X - 1, Y - 1]:
    for i in range(N):
        for j in range(N):
            # k経由でiからjへ
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

cnt = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        v = dp[i][j]
        cnt[v] += 1
for i in range(1, N):
    print(cnt[i])
