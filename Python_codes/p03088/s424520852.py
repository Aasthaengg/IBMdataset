#18:20
n = int(input())
mod = 10 ** 9 + 7
now = [[[[0 for _ in range(4)]
            for _ in range(4)]
            for _ in range(4)]
            for _ in range(4)]
now[3][3][3][3] = 1
for _ in range(n):
  last = now
  now = [[[[0 for _ in range(4)]
              for _ in range(4)]
              for _ in range(4)]
              for _ in range(4)]
  for i in range(4):
    for j in range(4):
      for k in range(4):
        for l in range(4):
          for m in range(4):
            now[j][k][l][m] += last[i][j][k][l]
            now[j][k][l][m] %= mod
  for j in range(4):
    now[j][0][1][2] = 0
    now[j][1][0][2] = 0
    now[j][0][2][1] = 0
  for k in range(4):
    now[0][k][1][2] = 0
  for l in range(4):
    now[0][1][l][2] = 0
ans = 0
for i in range(4):
  for j in range(4):
    for k in range(4):
      for l in range(4):
        ans += now[i][j][k][l]
print(ans % mod)