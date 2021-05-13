N = int(input())
p = list(map(float, input().split()))
dp = [[0.0 for i in range(N+1)] for _ in range(N+1)]
dp[0][0] = 1.0
for i in range(N):
    for j in range(i+1):
        # 表が出る
        dp[i+1][j+1] += dp[i][j] * p[i]
        # 裏が出る
        dp[i+1][j] += dp[i][j] * (1 - p[i])
temp = (N+1)//2
print(sum(dp[-1][temp:]))