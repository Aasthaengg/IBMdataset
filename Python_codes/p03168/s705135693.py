import random

n = int(input())
p = [float(i) for i in input().split()]

# dp[i][j] = i番目までのコインを振ったとき、表の数がj枚となる確率
dp = [[0.0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1.0

for i in range(n):
    for j in range(n):
        # 表のとき
        dp[i+1][j+1] += dp[i][j] * p[i]
        # 裏のとき
        dp[i+1][j] += dp[i][j] * (1 - p[i])

ans = sum(dp[-1][n//2+1:])
print(ans)
