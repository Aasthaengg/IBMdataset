H, W, K = map(int, input().split())
s = [input() for i in range(H)]

c = 1
div = [[0] * W for i in range(H)]
for i in range(H):
  for j in range(W):
    if s[i][j] == '#':
      div[i][j] = c
      c += 1

for i in range(H):
  for j in range(1, W):
    if div[i][j] == 0 and div[i][j-1] != 0:
      div[i][j] = div[i][j-1]
  for j in range(W-2, -1, -1):
    if div[i][j] == 0 and div[i][j+1] != 0:
      div[i][j] = div[i][j+1]

for i in range(1, H):
  for j in range(W):
    if div[i][j] == 0 and div[i-1][j] != 0:
      div[i][j] = div[i-1][j]

for i in range(H-2, -1, -1):
  for j in range(W):
    if div[i][j] == 0 and div[i+1][j] != 0:
      div[i][j] = div[i+1][j]

for d in div:
  print(*d)