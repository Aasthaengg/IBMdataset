S=input()
l=len(S)
dp=[[0,0,0] for i in range(l+2)]
dp[1][0]=dp[2][1]=1
for i in range(l):
    if(i>0 and S[i-1]!=S[i]):
        dp[i+1][1]=max(dp[i+1][1],dp[i][1]+1)
    if(i>=2 and S[i-2:i]!=S[i:i+2]):
        dp[i+2][2]=max(dp[i+2][2],dp[i][2]+1)
    dp[i+2][2]=max(dp[i+2][2],dp[i][1]+1)
    dp[i+1][1]=max(dp[i+1][1],dp[i][2]+1)
print(max(dp[l]))