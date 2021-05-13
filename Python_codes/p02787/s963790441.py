H, N = list(map(int, input().split()))
dp = [[float('inf')] * (H + 1)]
dp[0][0] = 0
magic = []
for i in range(N):
  magic.append(list(map(int, input().split())))
  
for i in range(H+1):
  next = dp[i]
  if dp[i][i] != float('inf'):
    for j in magic:
      next[min(H, i + j[0])] = min(dp[i-1][i] + j[1], dp[i][min(H, i + j[0])])
  dp.append(next)

print(dp[-1][-1])