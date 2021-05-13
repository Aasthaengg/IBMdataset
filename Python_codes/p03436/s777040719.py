from collections import deque
h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]
dhdw = [[-1,0],[1,0],[0,-1],[0,1]]
min_dis=[[-1]*w for _ in range(h)]
que=deque()
def bfs(x,y):
  que.append([x,y])
  min_dis[x][y]=0
  while que:
    sh,sw=que.popleft()
    for dh,dw in dhdw:
      nh,nw = sh+dh,sw+dw
      if not(0<=nh<=h-1) or not(0<=nw<=w-1) or min_dis[nh][nw]!=-1 or c[nh][nw]=='#':
        continue
      min_dis[nh][nw]=min_dis[sh][sw]+1
      que.append([nh,nw])
      if [nh,nw]==[h-1,w-1]:
        return min_dis[sh][sw]+1
a=bfs(0,0) or 0
if a==0:
  print(-1)
  exit()
ans=0
for i in c:
  ans+=i.count(".")
print(ans-1-a)