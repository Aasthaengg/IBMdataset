N=int(input())
*h,=map(int,input().split())
INF=10**12

dp = [0]*N

for i in range(1,N):
  if i == 1:
    dp[i] = dp[0] + abs(h[i]-h[0])
    continue
  dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
  
print(dp[-1])