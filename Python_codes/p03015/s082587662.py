l = input()

dp = [[0 for i in range(2)] for j in range(len(l)+1)]

mod = 10**9+7

dp[0][0] = 1

for i in range(len(l)):
    #a+b=0
    if l[i] == '0':
        dp[i+1][0] += dp[i][0]
        dp[i+1][0] %= mod
        dp[i+1][1] += dp[i][1]
        dp[i+1][1] %= mod
    else:
        dp[i+1][1] += (dp[i][0] + dp[i][1])%mod
        dp[i+1][1] %= mod
    #a+b=1
    if l[i] == '0':
        dp[i+1][1] += (dp[i][1] * 2) %mod
        dp[i+1][1] %= mod
    else:
        dp[i+1][0] += (dp[i][0] * 2)%mod
        dp[i+1][0] %= mod
        dp[i+1][1] += (dp[i][1]*2)%mod
        dp[i+1][1] %= mod
        
print((dp[len(l)][0]+dp[len(l)][1])%mod)
#print(dp)