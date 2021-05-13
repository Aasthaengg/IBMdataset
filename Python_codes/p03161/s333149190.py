N, K = map(int, input().split(' '))
h = [None] + list(map(int, input().split(' ')))

dp = [None for _ in range(N+1)]
# dp[0], dp[1], ..., dp[N] が用意される

dp[1] = 0
for k in range(2, N+1): # k = 2, ..., N
  candidate = []
  for i in range(1, K+1): # i = 1, 2, ..., K
    if k - i <= 0:
      break
    candidate.append(dp[k-i] + abs(h[k] - h[k-i]))
  dp[k] = min(candidate)

print(dp[N])

