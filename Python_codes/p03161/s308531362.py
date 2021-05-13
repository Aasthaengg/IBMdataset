N,K = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
dp = [10**10]*(N+1)
dp[1] = 0
dp[2] = abs(h[0] - h[1])

for i in range(3,N+1):
  Kl = max(1,i-K)
  dp[i] = min([dp[j]+abs(h[j-1] - h[i-1]) for j in range(Kl, i)])
print(dp[N])