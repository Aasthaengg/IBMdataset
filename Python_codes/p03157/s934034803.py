import sys
sys.setrecursionlimit(410000)

h,w = map(int,input().split())
F = []
for i in range(h):
  F.append(list(input()))
  
V = [[False]*w for _ in range(h)]

def dfs(y,x,c):      
  V[y][x] = True
  black = 0
  white = 0
  if c =='#':
    black+=1
  else:
    white+=1
  for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
    ny = y + dy
    nx = x + dx
    if 0<=ny<h and 0<=nx<w:      
      if F[ny][nx]!=c and V[ny][nx] == False:
        nc = '#'
        if c =='#':
          nc = '.'
        bn,wn = dfs(ny,nx,nc)
        black += bn
        white += wn  
  return black,white
        
ans = 0
for i in range(h):
  for j in range(w):
    if F[i][j] == '#':      
      black,white = dfs(i,j,'#')
      ans += black*white
      
print(ans)      