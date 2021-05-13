n = int(input())
mod = 10 ** 9 + 7
now = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
now[3][3][3][3] = 1
for _ in range(n):
  last = now
  now = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
  for i in range(4):
    for j in range(4):
      for k in range(4):
        for l in range(4):
          for m in range(4):
            now[j][k][l][m] += last[i][j][k][l]
            now[j][k][l][m] %= mod
  for h in range(4):
    now[h][0][1][2] = 0
    now[h][1][0][2] = 0
    now[h][0][2][1] = 0
    now[0][h][1][2] = 0
    now[0][1][h][2] = 0
ans = 0
for j in range(4):
  for k in range(4):
    for l in range(4):
      for m in range(4):
        ans += now[j][k][l][m]
        ans %= mod
print(ans)