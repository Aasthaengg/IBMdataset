x = int(input())
dp = [0]*(x + 105 + 1)
dp[100] = 1 
dp[101] = 1
dp[102] = 1
dp[103] = 1
dp[104] = 1
dp[105] = 1

for i in range(100,x+1):
    for j in range(100,106):
        dp[i+j] = max(dp[i] , dp[i+j])

print(dp[x])