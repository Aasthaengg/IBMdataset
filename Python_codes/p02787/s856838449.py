H, N = [int(i) for i in input().split()]
M = []
for i in range(N):
  A, B = [int(i) for i in input().split()]
  M.append((A, B))

dp = [0 for i in range(H + 1)]

for i in range(1, H+1):
  cand = []
  for A, B in M:
    cand.append(dp[max(0, i-A)] + B)
  dp[i] = min(cand)
print(dp[H])
