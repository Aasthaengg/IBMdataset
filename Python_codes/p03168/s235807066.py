n=int(input())
a=list(map(float,input().split()))

dp=[[0 for j in range (n+1)] for i in range (n+1)]

for i in range (n):
    if i>0:
        dp[i][0]=dp[i-1][0]*(1-a[i])
    else:
        dp[i][0]=(1-a[i])
    for j in range (1,i+2):
        if i>0:
            dp[i][j]=dp[i-1][j]*(1-a[i])+dp[i-1][j-1]*a[i]
        else:
            dp[i][j]=a[i]

x=int(n/2)
x=n-x
ans=0

for i in range (x,n+1):
   # print(x)
    ans+=dp[n-1][i]


print(ans)