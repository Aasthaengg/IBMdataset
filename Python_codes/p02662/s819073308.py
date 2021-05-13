import sys
readline = sys.stdin.readline

# Sのそれぞれの項目について
# (1)Tに属さない
# (2)Tに属すが計算に使われない
# (3)Tに属して計算に使われる
# の3通りがある

# dp[i][j] = i番目の数を処理したときに、合計がjになるものは何通りあるか

DIV = 998244353
N,S = map(int,readline().split())
A = list(map(int,readline().split()))

dp = [[0] * (S + 1) for i in range(N + 1)]

dp[0][0] = 1
for i in range(N):
  val = A[i]
  for j in range(len(dp[i]) - 1, -1, -1):
    if dp[i][j] == 0:
      continue
    dp[i + 1][j] += dp[i][j] * 2 # 使わない場合、選ばない場合
    dp[i + 1][j] %= DIV
    if j + val <= S:
      dp[i + 1][j + val] += dp[i][j]
      dp[i + 1][j + val] %= DIV
  
print(dp[-1][-1])