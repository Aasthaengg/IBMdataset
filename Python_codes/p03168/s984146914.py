n = int(input())
ns = list(map(float, input().split()))
dp = [[0 for j in range(n+1)] for i in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(0, i + 1):
        dp[i][j] = dp[i-1][j] * (1-ns[i-1]) + dp[i-1][j-1] * ns[i-1]
print(sum(dp[-1][(n+1)//2:]))