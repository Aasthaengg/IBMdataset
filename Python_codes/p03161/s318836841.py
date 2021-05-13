n,k = map(int, input().split())
H = [0]+list(map(int, input().split()))
dp = [float("inf")]*(n+1)
dp[0] = 0
dp[1] = 0

for i in range(1, n):
  for k_i in range(1, k+1):
    if i+k_i<=n:
      dp[i+k_i] = min(dp[i+k_i], dp[i]+abs(H[i+k_i]-H[i]))
      
print(dp[-1])