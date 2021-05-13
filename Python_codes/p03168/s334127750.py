n = int(input())
p = [float(x) for x in input().split()]

dp = [[0 for _ in range(n+1)] for __ in range(n+1)]

dp[0][0] = 1

for i in range(1,n+1):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = (1-p[i-1])*dp[i-1][j]
        else:
            dp[i][j] = (1-p[i-1])*dp[i-1][j] + p[i-1]*dp[i-1][j-1]

print(sum(dp[n][(n+1)//2:]))

