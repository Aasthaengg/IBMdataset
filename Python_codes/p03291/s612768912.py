s=input()
l=len(s)

dp=[[0]*3 for i in range(l)]
mod=10**9+7
c=0

for i in range(l):
    if s[i]=="A":
        dp[i][0]=dp[i-1][0]+pow(3,c,mod)
        dp[i][1]=dp[i-1][1]
        dp[i][2]=dp[i-1][2]
    elif s[i]=="B":
        dp[i][0]=dp[i-1][0]
        dp[i][1]=dp[i-1][1]+dp[i-1][0]
        dp[i][2]=dp[i-1][2]
    elif s[i]=="C":
        dp[i][0]=dp[i-1][0]
        dp[i][1]=dp[i-1][1]
        dp[i][2]=dp[i-1][2]+dp[i-1][1]
    else:
        dp[i][0]=dp[i-1][0]*3+pow(3,c,mod)
        dp[i][1]=dp[i-1][1]*3+dp[i-1][0]
        dp[i][2]=dp[i-1][2]*3+dp[i-1][1]
        c+=1
    dp[i][0]=dp[i][0]%mod
    dp[i][1]=dp[i][1]%mod
    dp[i][2]=dp[i][2]%mod

print(dp[-1][2])
