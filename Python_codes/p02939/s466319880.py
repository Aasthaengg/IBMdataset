s=input()
n=len(s)
dp=[[0]*2 for _ in range(n)]
dp[0]=[1,0]
# dp[1]=
for i in range(n):
    if i+1<n:
        dp[i+1][0]=max(dp[i+1][1],dp[i][1]+1)
        if s[i]!=s[i+1]:
            dp[i+1][0]=max(dp[i+1][0],dp[i][0]+1)
    if i+2<n:    
        dp[i+2][1]=max(dp[i+2][0],dp[i][0]+1)
        if s[i-1:i+1]!=s[i+1:i+3]:
            dp[i+2][1]=max(dp[i+2][1],dp[i][1]+1)
print(max(dp[-1]))