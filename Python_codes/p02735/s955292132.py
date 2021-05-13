h,w=map(int,input().split())
m=[]
grid=[]
nextdfsstart=set()
nextdfsstart.add(0)
def dfs(x,y,colour):
  global grid
  global nextdfsstartcopy
  global visited
  grid[y][x]=depth
  visited.add(x+w*y)
  if x<w-1 and not x+1+y*w in visited:
    if m[y][x+1]==colour :
      dfs(x+1,y,colour)
    else:
      nextdfsstartcopy.add(x+1+y*w)
  if y<h-1 and not x+(y+1)*w in visited:
    if m[y+1][x]==colour :
      dfs(x,y+1,colour)
    else:
      nextdfsstartcopy.add(x+(y+1)*w)
for i in range(h):
  m.append(input())
  grid.append([])
  for j in range(w):
      grid[i].append(-1)
visited=set()
depth=0
while grid[h-1][w-1]==-1:
  nextdfsstartcopy=set()
  for i in nextdfsstart:
    if i in visited:
      continue
    k=i//w
    if (k+1)*w<=i:
      k+=1
    dfs(i%w,k,m[k][i%w])
  depth+=1
  nextdfsstart=nextdfsstartcopy.copy()
ans=grid[h-1][w-1]//2
if m[0][0]=='#' or m[h-1][w-1]=='#':
  ans+=1
print(ans)