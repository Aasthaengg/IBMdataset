s= list(input())
n=len(s)

mod=10**9+7

ans=0
dp=[[0,0,0] for i in range(n+1)]
cnt=1

for i in range(n):
    if s[i]=='A':
        dp[i+1][0]=dp[i][0]+cnt
        dp[i+1][1]=dp[i][1]
        dp[i+1][2]=dp[i][2]
        dp[i+1][0]%=mod
    elif s[i]=='B':
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][1]+dp[i][0]
        dp[i+1][2]=dp[i][2]
        dp[i+1][1]%=mod
    elif s[i]=='C':
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][1]
        dp[i+1][2]=dp[i][2]+dp[i][1]
        dp[i+1][2]%=mod
    else:
        dp[i+1][0]=3*dp[i][0]+cnt
        dp[i+1][1]=3*dp[i][1]+dp[i][0]
        dp[i+1][2]=3*dp[i][2]+dp[i][1]
        cnt*=3
        cnt%=mod
        dp[i+1][0]%=mod
        dp[i+1][1]%=mod
        dp[i+1][2]%=mod

print(dp[-1][-1])