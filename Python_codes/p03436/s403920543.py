h,w=map(int,input().split())
g=[input() for _ in range(h)]
d=[[-1]*w for _ in range(h)]
d[0][0]=0
q=[(0,0)]
while q:
  tx,ty=q.pop(0)
  for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
    nx,ny=tx+dx,ty+dy
    if 0<=nx<h and 0<=ny<w and g[nx][ny]=='.' and d[nx][ny]<0:
      d[nx][ny]=d[tx][ty]+1
      q+=[(nx,ny)]
print((sum(s.count('.') for s in g)-d[-1][-1])*(d[-1][-1]>0)-1)