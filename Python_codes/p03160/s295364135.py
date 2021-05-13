N = int(input())

heights = [int(s) for s in input().split()]

def cost(i, j):
  return abs(heights[i] - heights[j])

dp = [0 for _ in range(N)]
dp[0] = 0
dp[1] = cost(0, 1)

if N > 3:
  for k in range(2, N):
    dp[k] = min(dp[k-1] + cost(k, k-1),
                dp[k-2] + cost(k, k-2))
print(dp[N-1])