N = int(input())
dp = [[0] * 3 for i in range(N + 1)]

for i in range(N):
  act = list(map(int,input().split()))
  for j in range(3):
    for a in range(len(act)):
      if a == j:
        continue
      if dp[i + 1][a] < dp[i][j] + act[a]:
        dp[i + 1][a] = dp[i][j] + act[a]

print(max(dp[-1]))
