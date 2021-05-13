h,w=map(int,input().split())
g=[input() for _ in range(h)]
a=[[0]*w for _ in range(h)]
for x in range(h):
  for y in range(w):
    if g[x][y]=='.': continue
    a[x][y]='#'
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]:
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and g[nx][ny]=='.':
        a[nx][ny]+=1
for l in a:
  print(*l,sep='')