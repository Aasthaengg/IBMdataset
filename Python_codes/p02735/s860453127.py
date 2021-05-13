h,w=map(int,input().split())
dp=[[0]*w for i in range(h)]
s=[input()for i in range(h)]
if s[0][0]=="#":
    dp[0][0]=1
for i in range(1,w):
    if s[0][i]=="#" and s[0][i-1]==".":
            dp[0][i]=dp[0][i-1]+1
    else:
        dp[0][i]=dp[0][i-1]
for i in range(1,h):
    for j in range(w):
        if j==0:
            if s[i][j]=="#" and s[i-1][j]==".":
                dp[i][j]=dp[i-1][j]+1
            else:
                dp[i][j]=dp[i-1][j]
            continue
        if s[i][j]=="#":
            p,q=0,0
            if s[i-1][j]=="#":
                p=1
            if s[i][j-1]=="#":
                q=1
            dp[i][j]=min(dp[i-1][j]-p,dp[i][j-1]-q)+1
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])