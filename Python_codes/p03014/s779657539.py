H,W = map(int,input().split())
Gd = [list(input()) for _ in range(H)]
L = [[0]*W for _ in range(H)]
R = [[0]*W for _ in range(H)]
U = [[0]*W for _ in range(H)]
D = [[0]*W for _ in range(H)]

for h in range(H):
  for w in range(W):
    if Gd[h][w]=='#':
      R[h][w]=0
    else:
      if w==0:
        R[h][w]=1
      else:
        R[h][w]=R[h][w-1]+1
    wr=W-w-1
    if Gd[h][wr]=='#':
      L[h][wr]=0
    else:
      if w==0:
        L[h][wr]=1
      else:
        L[h][wr]=L[h][wr+1]+1

for w in range(W):
  for h in range(H):
    if Gd[h][w]=='#':
      D[h][w]=0
    else:
      if h==0:
        D[h][w]=1
      else:
        D[h][w]=D[h-1][w]+1
    hr=H-h-1
    if Gd[hr][w]=='#':
      U[hr][w]=0
    else:
      if h==0:
        U[hr][w]=1
      else:
        U[hr][w]=U[hr+1][w]+1
ret = 0
for w in range(W):
  for h in range(H):
    ret = max(ret, D[h][w]+U[h][w]+R[h][w]+L[h][w]-3)
print(ret)
