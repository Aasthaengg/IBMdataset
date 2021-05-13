h,w=map(int,input().split())
maze=[list(input()) for i in range(h)]
distance=[[-1]*w for i in range(h)]

cnt=0
for i in maze:
  cnt+=i.count('#')

Q=[[0,0]]
distance[0][0]=1

ans=-1

while Q:
  p=Q.pop(0)
  if p[0]==h-1 and p[1]==w-1:
    ans=h*w-cnt-distance[h-1][w-1]
    break

  dx=[1,-1,0,0]
  dy=[0,0,1,-1]

  for i in range(4):
    nx=p[0]+dx[i]
    ny=p[1]+dy[i]

    if 0<=nx<h and 0<=ny<w and distance[nx][ny]==-1 and maze[nx][ny]!='#':
      Q.append([nx,ny])
      distance[nx][ny]=distance[p[0]][p[1]]+1

print(ans)
