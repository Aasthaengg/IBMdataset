X = int(input())

price = [100,101,102,103,104,105]
dp = [[0]*100001 for _ in range(6)]

dp[0][0] = 1
for i in range(100,100001):
    dp[0][i] = dp[0][i-100]

for i in range(1,6):
    for j in range(price[i]):
        dp[i][j] = dp[i-1][j]
    for j in range(price[i],100001):
        dp[i][j] = max(dp[i-1][j],dp[i][j-price[i]])

print(dp[-1][X])
