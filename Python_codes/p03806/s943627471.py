n, ma, mb = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
MAX_N = 10 * n + 1
dp = [[[float('inf')] * MAX_N for _ in range(MAX_N)] for _ in range(n + 1)]
dp[0][0][0] = 0

for k, (a, b, c) in enumerate(ls):
    for i in range(MAX_N):
        for j in range(MAX_N):
            dp[k + 1][i][j] = min(dp[k + 1][i][j], dp[k][i][j])
            if i + a < MAX_N and j + b < MAX_N:
                dp[k + 1][i + a][j + b] = min(dp[k][i][j] + c,
                                              dp[k][i + a][j + b])
p = min([
    dp[n][ma * i][mb * i] for i in range(1, MAX_N)
    if ma * i < MAX_N and mb * i < MAX_N
])
if p < float('inf'):
    print(p)
else:
    print(-1)