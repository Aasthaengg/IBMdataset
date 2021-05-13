L = input()
mod = 10**9+7
dp = [[0,0] for i in range(len(L)+1)] #[0]が=,[1]が以下
dp[0][0] = 2
dp[0][1] = 1
for i in range(len(L)-1):
    if L[i+1] == '0':
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = (dp[i][1]*3)%mod
    else:
        dp[i+1][0] = (dp[i][0]*2)%mod
        dp[i+1][1] = (dp[i][1]*3+dp[i][0])%mod
print((dp[len(L)-1][0]+dp[len(L)-1][1])%mod)