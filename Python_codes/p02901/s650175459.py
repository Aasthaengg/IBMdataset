# 15:20-

n, m = map(int, input().split())

dp = [[float("inf") for _ in range(2 ** n)] for i in range(m + 1)]
dp[0][0] = 0

pattern = {0}

for i in range(1, m+1):
  ai, bi = map(int, input().split()) 
  ci_bit = sum(2 ** (cij - 1) for cij in map(int, input().split()))
  new_pattern = set()
  for j in pattern:
    dp[i][j | ci_bit] = min(dp[i][j | ci_bit], dp[i-1][j] + ai)
    dp[i][j] = min(dp[i][j], dp[i-1][j])
    new_pattern.add(j | ci_bit)
  pattern |= new_pattern


print(-1 if dp[m][2**n - 1] == float("inf") else dp[m][2**n - 1])