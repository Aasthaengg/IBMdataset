MOD = 1000000007
L=input()
N=len(L)
dp=[[0,0] for i in range(N+1)]
dp[0][1]=1
for i in range(N):
    if L[i]=='1':
        dp[i+1][1]=dp[i][1]*2
        dp[i+1][1]%=MOD
        dp[i+1][0]=3*dp[i][0]+dp[i][1]
        dp[i+1][0]%=MOD
    if L[i]=='0':
        dp[i+1][1]=dp[i][1]
        dp[i+1][0]=3*dp[i][0]
        dp[i+1][0]%=MOD
print((dp[N][0]+dp[N][1])%MOD)