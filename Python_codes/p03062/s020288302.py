N = int(input())
A = list(map(int,input().split()))

# dp[i][j] = i個目とi - 1個目に対して、j(True:反転させた, False:元のまま)の状態でのi個目までの最大値

dp = [[0] * 2 for i in range(N)]

dp[0][False] = None
dp[0][True] = None
dp[1][False] = A[0] + A[1]
dp[1][True] = (A[0] + A[1]) * (-1)

for i in range(2, len(dp)):
  dp[i][False] = max(dp[i - 1][False] + A[i], dp[i - 1][True] + A[i])
  dp[i][True] = max(dp[i - 1][False] - A[i - 1] * 2 - A[i], dp[i - 1][True] + A[i - 1] * 2 - A[i])

print(max(dp[N - 1][False], dp[N - 1][True]))