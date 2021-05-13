n,u,v=map(int,input().split())
u-=1;v-=1
edge=[[]*n for _ in range(n)]
for _ in range(n-1):
  a,b=map(int,input().split())
  a-=1;b-=1
  edge[a].append(b)
  edge[b].append(a)
  
  
# from u 逃げる
# uはvからみた距離が大きい方に進むのかな
# from v 追う
# v始点でBFSして各頂点への距離を持つ
dist=[-1]*n

from collections import deque
q=deque()
q.append(v)
dist[v]=0
while q:
  p=q.popleft()
  d=dist[p]
  for i in edge[p]:
    if dist[i]==-1:
      dist[i]=d+1
      q.append(i)

# print(dist)

far=[-1]*n
q=deque()
q.append(u)
far[u]=0
while q:
  p=q.popleft()
  d=far[p]
  for i in edge[p]:
    if far[i]==-1:
      if dist[i]>d+1:
        far[i]=d+1
        q.append(i)

# print(far)
  

far_mx=max(far)
if far_mx==-1:
  print(0)
  exit()
  
ind=[i for i,v in enumerate(far) if v!=-1]

to=max(dist[i] for i in ind)
ans=(to-1)
print(ans)
