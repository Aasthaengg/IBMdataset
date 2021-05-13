N = int(input())
HS = [int(i) for i in input().split()]

dp = [float('inf')]*N

dp[0] = 0
dp[1] = abs(HS[1] - HS[0])

for i in range(2, N):
  dp[i] = min(dp[i-1] + abs(HS[i] - HS[i-1]), dp[i-2] + abs(HS[i] - HS[i-2]))

print(dp[N-1])
