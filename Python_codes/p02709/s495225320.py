n=int(input())
a=map(int,input().split())
p=[(x,i) for i,x in enumerate(a)]
p.sort(reverse=True)

ans=0
dp=[[0]*(n+1) for i in range(n+1)]
for i in range(n+1):
  for j in range(n+1):
    if i+j==n:
      ans=max(ans,dp[i][j])
      break
    act,ind=p[i+j]
    dp[i+1][j]=max(dp[i+1][j],
                   dp[i][j]+act*abs(ind-i))
    dp[i][j+1]=max(dp[i][j+1],
                   dp[i][j]+act*abs(n-1-j-ind))

print(ans)