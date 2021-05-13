import numpy as np
N, K = map(int, input().split(' '))
h = np.array([-1] + list(map(int, input().split(' '))), dtype=np.int64)

dp = np.array([-1 for _ in range(N+1)], dtype=np.int64)
# dp[0], dp[1], ..., dp[N] が用意される

dp[1] = 0
for k in range(2, N+1): # k = 2, ..., N
  """
  candidate = []
  for i in range(1, K+1): # i = 1, 2, ..., K
    if k - i <= 0:
      break
    candidate.append(dp[k-i] + abs(h[k] - h[k-i]))
  """
  start_index = max(1, k - K)
  # candidate = [
  #     dp[start_index] + abs(h[k] - h[start_index]),
  #     dp[start_index+1] + abs(h[k] - h[start_index+1]),
  #     ...,
  #     dp[k-1] + abs(h[k] - h[k-1]),
  # ]
  candidate = dp[start_index:k] + np.abs(h[k] - h[start_index:k])
  dp[k] = np.min(candidate)
  # print("candidate: ", candidate)
  # print("dp[{}]=={}".format(k, dp[k]))

print(dp[N])
