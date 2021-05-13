import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())
grid = [readline().rstrip() for i in range(H)]

# 各マスについて、上下左右にそれぞれ照射できるマスがいくつあるか
L = [[0] * W for i in range(H)]
R = [[0] * W for i in range(H)]
U = [[0] * W for i in range(H)]
D = [[0] * W for i in range(H)]

for i in range(H):
  cur = 0
  for j in range(W):
    if grid[i][j] == "#":
      cur = 0
    else:
      cur += 1
    L[i][j] = cur
  cur = 0
  for j in range(W - 1,-1,-1):
    if grid[i][j] == "#":
      cur = 0
    else:
      cur += 1
    R[i][j] = cur
    
for j in range(W):
  cur = 0
  for i in range(H):
    if grid[i][j] == "#":
      cur = 0
    else:
      cur += 1
    U[i][j] = cur
  cur = 0
  for i in range(H - 1,-1,-1):
    if grid[i][j] == "#":
      cur = 0
    else:
      cur += 1
    D[i][j] = cur
    
ans = 0
for i in range(H):
  for j in range(W):
    if ans < L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3:
      ans = L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3
      
print(ans)