n = int(input())
MOD = 10**9+7
# dp[i][j][k][l]:文字列長iで,後ろから3文字目がj,2文字目がk,1文字目がlの文字列の個数
#                ただしA:0,C:1,G:2,T:3とする。
dp= [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(101)]
# 文字列長0の文字列Sは、333+Sと考えてよい。
dp[0][3][3][3] = 1
for i in range(100):
  for j in range(4):
    for k in range(4):
      for l in range(4):
        #if dp[i][j][k][l] == 0:
        #  continue
        for m in range(4):
          # 条件を満たさないパターンを除外する。
          # 条件を満たさないのは、文字列の末尾が下記の場合。
          # 021,201,021,0?21,02?1
          if k == 0 and l == 2 and m == 1:
            continue
          if k == 2 and l == 0 and m == 1:
            continue
          if k == 0 and l == 1 and m == 2:
            continue
          if j == 0 and l == 2 and m == 1:
            continue
          if j == 0 and k == 2 and m == 1:
            continue
          dp[i+1][k][l][m] += dp[i][j][k][l]
          dp[i+1][k][l][m] %= MOD
ans = 0
for j in range(4):
  for k in range(4):
    for l in range(4):
      ans += dp[n][j][k][l]
      ans %= MOD
print(ans)            