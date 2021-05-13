h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
dp=[[0]*w for _ in range(h)]
if s[0][0]=="#":
    dp[0][0]=1
for i in range(w-1):
    if s[0][i]=="." and s[0][i+1]=="#":
        dp[0][i+1]=dp[0][i]+1
    else:
        dp[0][i+1]=dp[0][i]
for i in range(h-1):
    if s[i][0]=="." and s[i+1][0]=="#":
        dp[i+1][0]=dp[i][0]+1
    else:
        dp[i+1][0]=dp[i][0]
for i in range(1,h):
    for j in range(1,w):
        v=0
        g=0
        if s[i-1][j]=="." and s[i][j]=="#":
            v=1
        if s[i][j-1]=="." and s[i][j]=="#":
            g=1

        dp[i][j]=min(dp[i-1][j]+v,dp[i][j-1]+g)
print(dp[h-1][w-1])
