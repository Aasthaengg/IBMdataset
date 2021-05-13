n,m=map(int,input().split())
A=list(map(int,input().split()))
L=[0,2,5,5,4,5,6,3,7,6]
dp=[0]+[-1]*n
for i in range(n+1):
  for a in A:
    if i+L[a]<=n:
      dp[i+L[a]]=max(dp[i+L[a]],dp[i]*10+a)
print(dp[n])
