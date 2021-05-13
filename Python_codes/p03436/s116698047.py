from collections import deque
h,w=[int(x) for x in input().split()]
c=[]
b=0
for i in range(h):
  C=input()
  b+=C.count("#")
  c.append(C)

dist=[[0]*w for i in range(h)]
dist[0][0]=1
d=deque()
d.append([0,0])

dydx=[[1,0],[0,1],[-1,0],[0,-1]]

while d:
  y,x=d.popleft()
  if y==h-1 and x==w-1:
    break
  for i in range(4):
    ny,nx=y+dydx[i][0],x+dydx[i][1]
    if not(0 <= ny < h) or not(0 <= nx < w) or dist[ny][nx]!=0 or c[ny][nx]=="#":
      continue
    dist[ny][nx]=dist[y][x]+1
    d.append([ny,nx])

if dist[h-1][w-1]==0:
  print(-1)
else:
  ans=h*w-b-dist[h-1][w-1]
  print(ans)