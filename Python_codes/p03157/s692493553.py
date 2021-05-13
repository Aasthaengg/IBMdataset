import sys
sys.setrecursionlimit(200000)
def dfs(x,y):
  vis[x][y]=1
  now=s[x][y]
  b=now=='#'
  w=now=='.'
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if not(0<=nx<r and 0<=ny<c) or vis[nx][ny] or s[nx][ny]==now:continue
    black,white=dfs(nx,ny)
    b+=black
    w+=white
  return b,w
r,c=map(int,input().split())
s=[input() for _ in range(r)]
vis=[[0]*c for _ in range(r)]
ans=0
dx=(-1,0,1,0)
dy=(0,-1,0,1)
for i in range(r):
  for j in range(c):
    if vis[i][j]:continue
    b,w=dfs(i,j)
    ans+=b*w
print(ans)