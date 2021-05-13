n,m,q=map(int,input().split())
grid=[]
for i in range(n+1):
  grid.append([])
  for j in range(n+1):
    grid[-1].append(0)
grid2=[]
for i in range(n+1):
  grid2.append([])
  for j in range(n+1):
    grid2[-1].append(0)
for i in range(m):
  l,r=map(int,input().split())
  grid[r][l]+=1
for sumxy in range(0,2*n+1):
  if sumxy>n:
    r=sumxy-n
  else:
    r=0
  for x in range(r,min(sumxy+1,n+1)):
    y=sumxy-x
    grid2[x][y]=grid2[x-1][y]+grid2[x][y-1]-grid2[x-1][y-1]+grid[x][y]
for i in range(q):
  p1,q1=map(int,input().split())
  print(grid2[q1][n]-grid2[q1][p1-1])