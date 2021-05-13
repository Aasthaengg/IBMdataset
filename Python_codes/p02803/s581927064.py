h,w = map(int,input().split())
l=[]

for i in range(h):
  s=[x for x in input()]
  l.append(s)

move=[[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y):
  done=[[-1 for i in range(w)] for j in range(h)]
  ans,cnt = 0,0
  que=[[x,y,cnt]]
  done[y][x]=0

  while(que):
    nx,ny,cnt = que.pop(0)

    for dx,dy in move:
      mx=nx+dx
      my=ny+dy

      if 0<=mx<w and 0<=my<h and done[my][mx]==-1 and l[my][mx]==".":
        done[my][mx]=cnt+1
        que.append([mx,my,cnt+1])
        ans=max(ans,cnt+1)

  return ans


ans_r=0
for i in range(w):
  for j in range(h):
    if l[j][i]==".":
      now=bfs(i,j)
      ans_r=max(now,ans_r)
print(ans_r)
