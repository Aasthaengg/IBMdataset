MOD=998244353
n,s=map(int,input().split())
a=list(map(int,input().split()))
al=sum(a)
dp=[[0]*3001 for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(3001):
        if j==0:
            dp[i+1][j]=pow(2,i+1,MOD)
            continue
        dp[i+1][j]=(dp[i+1][j]+(dp[i][j]*2%MOD))%MOD
        if j-a[i]>=0:
            dp[i+1][j]=(dp[i+1][j]+dp[i][j-a[i]])%MOD
print(dp[n][s])