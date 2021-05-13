n = int(input())
p = list(map(float, input().split()))

dp = [[0] * (n + 2) for i in range(n)]
dp[0][1] = 1 - p[0]
dp[0][2] = p[0]

for i in range(1, n):
    for j in range(1, i + 3):
        dp[i][j] = dp[i - 1][j - 1] * p[i] + dp[i - 1][j] * (1 - p[i])

ans = 0
for i in range(n//2 + 2, n + 2):
    ans += dp[n - 1][i]

print(ans)