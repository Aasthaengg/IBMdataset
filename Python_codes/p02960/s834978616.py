s=list(input())
mod=10**9+7
n=len(s)
for i in range(n):
    if s[i]!="?":
        s[i]=int(s[i])
dp=[[0]*13 for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    if s[i]=="?":
        for k in range(10):
            for j in range(13):
                p=(k+10*j)%13
                dp[i+1][p]+=dp[i][j]
                dp[i+1][p]%=mod

    else:
        for j in range(13):
            p=(s[i]+10*j)%13
            dp[i+1][p]+=dp[i][j]
            dp[i+1][p]%=mod
print(dp[n][5])
