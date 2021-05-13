n=int(input())
a=list(map(int,input().split()))

# dp には 足場(i)へ至る最小コストが入る。
dp=[float("inf")]*(n)
dp[0]=0
for i in range(n-1):
  dp[i+1]=min(dp[i+1],dp[i]+abs(a[i]-a[i+1]))
  if i+2 < n:
    dp[i+2]=min(dp[i+2],dp[i]+abs(a[i]-a[i+2]))
    
print(dp[-1])
    

