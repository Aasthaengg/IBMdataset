l = input()
dp = [[0 for j in range(2)] for k in range(len(l)+1)]
dp[0][0] = 1
for i in range(len(l)):
    #a+b=1
    if l[i] == '0':
        dp[i+1][1] = dp[i][1]*2
    else:
        dp[i+1][1] = dp[i][1]*2
        dp[i+1][0] = dp[i][0]*2
    
    #a+b = 0
    if l[i] == '0':
        dp[i+1][1] += dp[i][1]
        dp[i+1][0] += dp[i][0]
    else:
        dp[i+1][1] += dp[i][1]+dp[i][0]
        
    dp[i+1][1] %= 10**9+7
    dp[i+1][0] %= 10**9+7
print((dp[len(l)][0]+dp[len(l)][1])%(10**9+7))