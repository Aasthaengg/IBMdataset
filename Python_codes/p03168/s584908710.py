N = int(input())
p = list(map(float,input().split()))

dp = [[0.0]*(N+1) for i in range(N+1)]
dp[0][0] = 1.0

for i in range(1,N+1):
    for j in range(0,N+1):
        dp[i][j] = dp[i-1][j-1]*(p[i-1]) + dp[i-1][j]*(1-p[i-1])

res = 0.0
for i in range((N+1)//2,N+1):
    res += dp[-1][i]
print(res)