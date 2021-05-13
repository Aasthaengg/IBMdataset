n=int(input())
l6=[6**i for i in range(7)]
l9=[9**i for i in range(1,6)]
m=l6+l9
m.sort()
inf=float("inf")
dp=[inf]*(10**5+1)
dp[0]=0
dp[1]=1
for i in range(1,n+1):
  for mi in m:
    if i-mi>=0:
      dp[i]=min(dp[i-mi]+1,dp[i])
print(dp[n])
