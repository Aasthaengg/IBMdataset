import sys
sys.setrecursionlimit(10**6)
H,W = map(int,input().split())
grid = []
for _ in range(H):
  grid.append(list(input()))

L = [ [0]*W for _ in range(H) ]
R = [ [0]*W for _ in range(H) ]
U = [ [0]*W for _ in range(H) ]
D = [ [0]*W for _ in range(H) ]

for i in range(H):
  for j in range(W):
    if j-1 >= 0:
      L[i][j] = L[i][j-1]
    if i-1 >= 0:
      D[i][j] = D[i-1][j]

    if grid[i][j] == ".":
      L[i][j] += 1
      D[i][j] += 1
    else:
      L[i][j] = 0
      D[i][j] = 0

for i in range(H-1,-1,-1):
  for j in range(W-1,-1,-1):
    if j+1 < W:
      R[i][j] = R[i][j+1] 
    if i+1 < H:
      U[i][j] = U[i+1][j]
    if grid[i][j] == ".":
      R[i][j] += 1
      U[i][j] += 1
    else:
      R[i][j] = 0
      U[i][j] = 0

res = 0
for i in range(H):
  for j in range(W):
    if grid[i][j] == ".":
      res = max(res, L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)

print(res)