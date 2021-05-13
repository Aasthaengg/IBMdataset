import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
S = list(map(int,readline().split()))
T = list(map(int,readline().split()))
DIV = 10 ** 9 + 7

# dp[i][j] = Sのi文字目、Tのj文字目まで見たときの組み合わせ総数
# dp[i][j] に対してはdp[i - 1][j - 1]の数がdp[i - 1][j]からきた数とdp[i][j - 1]から来たのでダブルカウントされている
# 従い、
# dp[i][j] += dp[i][j - 1]
# dp[i][j] += dp[i - 1][j]
# をした後で、ダブルカウント分を
# dp[i][j] -= dp[i - 1][j - 1]
# 引く(i > 0 and j > 0)
# S[i] == T[j]の場合、dp[i - 1][j - 1]から直接遷移することが出来るので、この通り数を足したうえでダブルカウントを引く
# ので、結局S[i] == T[j]の場合はダブルカウント分を引かないのと同じ挙動になる

dp = [[0] * (M + 1) for i in range(N + 1)]

for i in range(N + 1):
  dp[i][0] = 1
for j in range(M + 1):
  dp[0][j] = 1

for i in range(1, N + 1):
  for j in range(1, M + 1):
    dp[i][j] += dp[i][j - 1]
    dp[i][j] += dp[i - 1][j]
    if S[i - 1] != T[j - 1]:
      dp[i][j] -= dp[i - 1][j - 1]
    dp[i][j] %= DIV

print(dp[-1][-1])