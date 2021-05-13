N = int(input())
C = [int(input()) for _ in range(N)]
MOD = 10**9+7

# PreStore:先頭から順に見ていったとき、その色と同じ色の石が前回現れた位置。
PreStone = [-1 for _ in range(2*(10**5))]

# 先頭から順に見ていったとき、ある色が現れ、次に同じ色が現れたとき、
# 前者と後者の間の色を変えるパターンが追加されるわけだから、
# 追加されるパターンの数は、前者が現れた時点でのパターン数と同じ。
# ただし、前者と後者の間には1つ以上の石が存在する必要がある。
dp = [1 for _ in range(N)]
for i in range(N):
  if PreStone[C[i]-1] not in [-1, i-1]:
    dp[i] = dp[i-1] + dp[PreStone[C[i]-1]]
  else:
    dp[i] = dp[i-1]
  dp[i] %= MOD
  PreStone[C[i]-1] = i
print(dp[-1])
