H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
a = [[-1]*W for _ in range(H)]
for i in range(H):
  for j in range(W):
    if s[i][j] == ".":
      a[i][j] = 1
    dh = [-1,0,1,0]
    dw = [0,-1,0,1]
    for k in range(4):
      ii = i + dh[k]
      jj = j + dw[k]
      if 0 <= ii < H and 0 <= jj < W:
        if s[i][j] == "#" and s[ii][jj] == "#":
          a[i][j] = 1
          a[ii][jj] = 1
flag = True
for i in range(H):
  for j in range(W):
    if a[i][j] != 1:
      flag = False
      break
if flag:
  print("Yes")
else:
  print("No")