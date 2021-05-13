h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

toUP = [[0] * w for _ in range(h)]
for i in range(w):
  cnt = 0
  for j in range(h):
    if S[j][i] == ".":
      cnt += 1
      toUP[j][i] = cnt
    else:
      cnt = 0

toDOWN = [[0] * w for _ in range(h)]
for i in range(w):
  cnt = 0
  for j in range(h - 1, -1, -1):
    if S[j][i] == ".":
      cnt += 1
      toDOWN[j][i] = cnt
    else:
      cnt = 0

toLEFT = [[0] * w for _ in range(h)]
for i in range(h):
  cnt = 0
  for j in range(w):
    if S[i][j] == ".":
      cnt += 1
      toLEFT[i][j] = cnt
    else:
      cnt = 0
    
toRIGHT = [[0] * w for _ in range(h)]
for i in range(h):
  cnt = 0
  for j in range(w - 1, -1, -1):
    if S[i][j] == ".":
      cnt += 1
      toRIGHT[i][j] = cnt
    else:
      cnt = 0

ans = 0
for i in range(h):
  for j in range(w):
    if S[i][j] == ".":
      ans = max(ans, toUP[i][j] + toDOWN[i][j] + toLEFT[i][j] + toRIGHT[i][j] - 3)
print(ans)
