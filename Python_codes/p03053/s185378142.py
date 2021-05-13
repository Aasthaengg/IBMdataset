H, W = map(int, input().split())
S = [input() for i in range(H)]
A = [[0 for j in range(W)] for i in range(H)]
pos = []
for i in range(H):
  for j in range(W):
    if S[i][j] == '#':
      pos.append([i, j])
      A[i][j] = 1
cnt = 0
while pos != []:
  n = len(pos)
  cnt += 1
  for i in range(n):
    x, y = pos[i][0], pos[i][1]
    if x > 0:
      if A[x-1][y] == 0:
        A[x-1][y] = 1
        pos.append([x-1, y])
    if x < H-1:
      if A[x+1][y] == 0:
        A[x+1][y] = 1
        pos.append([x+1, y])
    if y > 0:
      if A[x][y-1] == 0:
        A[x][y-1] = 1
        pos.append([x, y-1])
    if y < W-1:
      if A[x][y+1] == 0:
        A[x][y+1] = 1
        pos.append([x, y+1])
  pos = pos[n:]
print(cnt-1)