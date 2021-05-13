
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
moves = ((1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1,1))
c = [[0]*W for _ in range(H)]
for i in range(H):
  for j in range(W):
    cnt = 0
    if S[i][j] == "#":
      c[i][j] = "#"
      continue
    for dy, dx in moves:
      ny = i + dy
      nx = j + dx
      if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '#':
        cnt += 1
    c[i][j] = cnt

for i in c:
  i = list(map(str, i))
  print("".join(i))