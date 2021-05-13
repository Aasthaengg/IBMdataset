n,k  = map(int,input().split())
h = list(map(int,input().split()))

dp = [0]*(n+1)
dp[0] = 0

for i in range(1,n):
  dp[i] = dp[i-1] + abs(h[i]-h[i-1])
  for j in range(2,min(i+1,k+1)):
    dp[i] = min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))    
  #print(dp[i])
print(dp[n-1])