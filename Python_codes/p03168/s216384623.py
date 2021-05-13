n = int(input())
p = [float(i) for i in input().split()]

dp = [[0 for i in range(n+1)] for j in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(n+1):
        if not j:
            dp[i+1][j] = dp[i][j]*(1-p[i])
        else:
            dp[i+1][j] = dp[i][j]*(1-p[i]) + dp[i][j-1]*p[i]

print(sum(dp[n][((n+1)//2):]))