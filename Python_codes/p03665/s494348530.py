# AGC017 A Biscuits

n, p = map(int, input().split())
a_list = [int(x)%2 for x in input().split()]

dp = [[0] * 2 for x in range(n+1)]
if a_list[0] == 0:
    dp[0][0] = 1
else:
    dp[0][1] = 1

for i in range(n):
    _a = a_list[i]
    if _a == 0:
        dp[i+1][0] = dp[i][0]*2
        dp[i+1][1] = dp[i][1]*2
    else:
        dp[i+1][0] = dp[i][1]+dp[i][0]
        dp[i+1][1] = dp[i][1]+dp[i][0]
        
print(dp[n][p])        