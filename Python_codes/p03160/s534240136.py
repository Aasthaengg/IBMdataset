N=int(input())

h=list(map(int,input().split()))
INF=10**10
dp=[INF]*N
dp[0]=0
for i in range(N):
  if i-1>=0:
    dp[i]=min(dp[i],dp[i-1]+abs(h[i]-h[i-1]))
  if i-2>=0:
    dp[i]=min(dp[i],dp[i-2]+abs(h[i]-h[i-2]))
print(dp[-1])