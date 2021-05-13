h,n=map(int,input().split())
a=[0]
b=[0]
width=2*10**4+7
dp=[[10**10 for i in range(width)] for j in range(n+1)]
dp[0][0]=0
dp[1][0]=0
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
for i in range(1,n+1):
    for j in range(width):
        dp[i][j]=min(dp[i][j],dp[i-1][j])
        if(j+a[i]<width):
            dp[i][j+a[i]]=min(dp[i][j+a[i]],dp[i][j]+b[i])
print(min(dp[n][h:]))