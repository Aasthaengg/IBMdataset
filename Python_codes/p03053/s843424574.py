H, W = map(int, input().split())
S = [input() for i in range(H)]
A = [[0 for j in range(W)] for i in range(H)]
pos = []
cnt = 0
for i in range(H):
  for j in range(W):
    if S[i][j] == '#':
      pos.append([i, j])
      A[i][j] = 1
      cnt += 1
ccnt = 0
pnt = 0
while pnt < cnt:
  n = cnt
  ccnt += 1
  for i in range(pnt, cnt):
    x, y = pos[i][0], pos[i][1]
    if x > 0:
      if A[x-1][y] == 0:
        A[x-1][y] = 1
        pos.append([x-1, y])
        cnt += 1
    if x < H-1:
      if A[x+1][y] == 0:
        A[x+1][y] = 1
        pos.append([x+1, y])
        cnt += 1
    if y > 0:
      if A[x][y-1] == 0:
        A[x][y-1] = 1
        pos.append([x, y-1])
        cnt += 1
    if y < W-1:
      if A[x][y+1] == 0:
        A[x][y+1] = 1
        pos.append([x, y+1])
        cnt += 1
  pnt = n
print(ccnt-1)