N,K=map(int,input().split())
*h,=map(int,input().split())

dp = [0]*N

for i in range(1,N):
  if i <= K:
    dp[i] = min([dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,i+1)])
  else:
    dp[i] = min([dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,K+1)])
    
print(dp[-1])