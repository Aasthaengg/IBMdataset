N,K=map(int, input().split())
*h,=map(int,input().split())
INF=10**12

dp = [INF]*N
dp[0]=0

for i in range(1,N):
  if i <= K:
    dp[i] = min([dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,i+1)])
  else:
    dp[i] = min([dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,K+1)])
  
print(dp[-1])