n = int(raw_input())
p = list(map(float, raw_input().split()))

dp = [[0]*(i+2) for i in range(n)]
dp[0][0] = 1-p[0]
dp[0][1] = p[0]

for i in range(1, n):
    for j in range(i+2):
        if j < i+1:
            dp[i][j] += dp[i-1][j]*(1-p[i])
        if j > 0:
            dp[i][j] += dp[i-1][j-1] * p[i]

print(sum(dp[n-1][(n//2)+1:]))
