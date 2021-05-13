from itertools import*
(n,), *D = [list(map(int, o.split())) for o in open(0)]
dp = [[0]*3 for _ in [None]*-~n]
for i in range(n):
  for j, k in permutations(range(3), 2):
    dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + D[i][k])
print(max(dp[n]))