s=input()
n=len(s)
dp=[[0]*(13) for _ in range(n)]
mod=10**9+7

for i in range(n):
    if i==0:
        if s[i]=='?':
            for j in range(10):
                dp[i][j]=1
        else:
            x=int(s[i])
            dp[i][x]=1
    else:
        if s[i]=='?':
            for k in range(10):
                for j in range(13):
                    dp[i][(j*10+k)%13]+=dp[i-1][j]
                    dp[i][(j*10+k)%13]%=mod
        else:
            x=int(s[i])
            for j in range(13):
                dp[i][(j*10+x)%13]+=dp[i-1][j]
                dp[i][(j*10+x)%13]%=mod
print(dp[n-1][5]%mod)