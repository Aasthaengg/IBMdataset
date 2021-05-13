h,w=map(int,input().split())
g=[input() for _ in range(h)]
for x in range(h):
  for y in range(w):
    if g[x][y]=='.': continue
    ng=1
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w:
        if g[nx][ny]=='#': ng=0
    if ng:
      print('No')
      exit()
print('Yes')