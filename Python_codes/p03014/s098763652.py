h,w = map(int,input().split())
F = [input() for _ in range(h)]

MW = [[0]*w for _ in range(h)]
MH = [[0]*w for _ in range(h)]


for i in range(h):
  l = 0
  c = 0
  for r in range(w):    
    if F[i][r] == '#':
      for k in range(l,r):
        MW[i][k] = c
      l = r+1
      c = 0      
    else:
      c += 1
  for k in range(l,r+1):
    MW[i][k] = c  
    
for i in range(w):
  u = 0
  c = 0
  for b in range(h):    
    if F[b][i] == '#':
      for k in range(u,b):
        MH[k][i] = c
      u = b+1
      c = 0      
    else:
      c += 1
  for k in range(u,b+1):
    MH[k][i] = c      
    
ans = 0    
for i in range(h):
  for j in range(w):
    tmp = 0
    if F[i][j] != '#':
      tmp = MH[i][j]+MW[i][j] -1 
    ans = max(ans,tmp)
    
print(ans)