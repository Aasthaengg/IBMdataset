inf=10**9+7
n=int(input())
h=list(map(int,input().split()))

dp=[inf]*n
dp[0]=0
for i in range(n):
  for j in range(i+1,i+3):
    if j<n:
      dp[j]=min(dp[j],dp[i]+abs(h[i]-h[j]))
      
print(dp[-1])