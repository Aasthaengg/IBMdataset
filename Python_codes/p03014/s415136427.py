H, W = map(int, input().split())
mp = ['#'*(W+2)]
for _ in range(H):
  mp.append('#'+input()+'#')
mp.append('#'*(W+2))

L = [[0]*(W+2) for _ in range(H+2)]
R = [[0]*(W+2) for _ in range(H+2)]
U = [[0]*(W+2) for _ in range(H+2)]
D = [[0]*(W+2) for _ in range(H+2)]

rlt = 0
for i in range(H+1):
  for j in range(W+1):
    if mp[i+1][j] == '#':
      D[i+1][j] = 0
    else:
      D[i+1][j] = D[i][j] + 1
    if mp[H-i][j] == '#':
      U[H-i][j] = 0
    else:
      U[H-i][j] = U[H-i+1][j] + 1 
    if mp[i][j+1] == '#':
      R[i][j+1] = 0
    else:
      R[i][j+1] = R[i][j] + 1
    if mp[i][W-j] == '#':
      L[i][W-j] = 0
    else:
      L[i][W-j] = L[i][W-j+1] + 1 

for i in range(1,H+1):
  for j in range(1,W+1):
    tmp = L[i][j]+R[i][j]+U[i][j]+D[i][j]-3
    if tmp > rlt:
      rlt = tmp
      
print(rlt)