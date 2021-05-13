N, K = [int(i) for i in input().split()]
HS = [int(i) for i in input().split()]

dp = [float('inf')]*N

dp[0] = 0
dp[1] = abs(HS[1] - HS[0])

for i in range(2, N):
  dp[i] = min([dp[i-k] + abs(HS[i] - HS[i-k]) for k in range(1, K + 1)])

print(dp[N-1])
