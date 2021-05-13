
mod = 1000000007
N = int(input())

dp = [ [[[0 for c3 in range(4)]  for c2 in range(4)]  for c1 in range(4)] for n in range(N+1)]

# 全部TのときはOK
dp[0][3][3][3] = 1

# 文字の数
for n in range(N):
  # 後ろから1文字目
  for c1 in range(4):
    # 後ろから2文字目
    for c2 in range(4):
      # 後ろから3文字目
      for c3 in range(4):
        # 該当するものがないとき
        if dp[n][c1][c2][c3] == 0: continue

        # 新しく追加する文字
        for a in range(4):
          # AGCに当てはまる文字
          if(c2 == 0 and c1 == 1 and a == 2): continue
          if(c2 == 0 and c1 == 2 and a == 1): continue
          if(c2 == 1 and c1 == 0 and a == 2): continue
          if(c3 == 0 and c1 == 1 and a == 2): continue
          if(c3 == 0 and c2 == 1 and a == 2): continue

          dp[n+1][a][c1][c2] += dp[n][c1][c2][c3]
          dp[n+1][a][c1][c2] %= mod

ans = 0
# 後ろから1文字目
for c1 in range(4):
  # 後ろから2文字目
  for c2 in range(4):
    # 後ろから3文字目
    for c3 in range(4):
      ans += dp[N][c1][c2][c3]
      ans %= mod

print(ans)