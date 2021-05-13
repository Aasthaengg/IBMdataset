n = int(input())

heads = list(map(float, input().split()))

dp = []

for i in range(n+1):
    temp = []
    for j in range(n+1):
        temp.append(0.0)
    
    dp.append(temp)

dp[0][0] = 1.0

for i in range(1, n+1):
    for j in range(0, n+1):
        dp[i][j] = dp[i-1][j] * (1-heads[i-1]) + dp[i-1][j-1] * heads[i-1]


ans = 0
for i in range((n+1)//2, n+1):
    ans += dp[n][i]

print(ans)