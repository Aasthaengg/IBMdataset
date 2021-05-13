N,K=map(int,input().split())

h=list(map(int,input().split()))
INF=10**10
dp=[INF]*N
dp[0]=0

for i in range(N):
  for j in range(1,K+1):
    if i-j>=0:
      dp[i]=min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
print(dp[-1])