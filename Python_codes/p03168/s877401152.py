N, = map(int, input().split())
Ps = map(float, input().split())
dp = [[0]*(N+1)for _ in range(N+1)]
dp[0][0] = 1
for i, p in enumerate(Ps):
    for j in range(N+1):
        dp[i+1][j] = p*dp[i][j-1] + (1-p)*dp[i][j]
r = 0
for i in range(N, N//2, -1):
    r += dp[N][i]
print(r)
