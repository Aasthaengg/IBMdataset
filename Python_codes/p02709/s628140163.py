n=int(input())
a_=list(map(int,input().split()))
a=[[i+1,ai] for i,ai in enumerate(a_)]
a.sort(key=lambda x:x[1],reverse=True)
dp=[[0]*(n+1) for _ in range(n+1)]
# dp[i][j]:大きい順にi+j人のうち、i人を左に、j人を右に移した時の最大値。
dp[1][0]=a[0][1]*abs(a[0][0]-1)
dp[0][1]=a[0][1]*abs(a[0][0]-n)
for k in range(2,n+1):
    for i in range(k+1):
        j=k-i
        if j==0:
            dp[i][j]=dp[i-1][j]+a[i+j-1][1]*abs(a[i+j-1][0]-i)
        elif i==0:
            dp[i][j]=dp[i][j-1]+a[i+j-1][1]*abs(n-a[i+j-1][0]-j+1)
        else:
            dp[i][j]=max(dp[i-1][j]+a[i+j-1][1]*abs(a[i+j-1][0]-i),dp[i][j-1]+a[i+j-1][1]*abs(n-a[i+j-1][0]-j+1))
ans=0
for i in range(n+1):
    ans=max(dp[i][n-i],ans)
print(ans)

