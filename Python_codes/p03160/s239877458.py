N = int(input())
h = [int(i) for i in input().split()]
dp = [99999]*(N+1)
dp[1] = 0
dp[2] = abs(h[0] - h[1])

for i in range(3,N+1):
  dp[i] = min(dp[i-2]+abs(h[i-1] - h[i-3]), dp[i-1]+ abs(h[i-2] - h[i-1]))
print(dp[N])