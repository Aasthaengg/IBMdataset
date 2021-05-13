n=int(input())
s=[input() for _ in range(2)]
mod=1000000007
dp=[0]*n
if s[0][0]==s[1][0]:
    dp[0]=3
else:
    dp[0]=6
for i in range(1,n):
    if s[0][i]==s[1][i]:
        if s[0][i-1]==s[1][i-1]:
            dp[i]=dp[i-1]*2%mod
        else:
            dp[i]=dp[i-1]
    else:
        if s[0][i-1]==s[1][i-1]:
            dp[i]=dp[i-1]*2%mod
        else:
            if s[0][i]==s[0][i-1]:
                dp[i]=dp[i-1]
            else:
                dp[i]=dp[i-1]*3%mod
print(dp[-1])
