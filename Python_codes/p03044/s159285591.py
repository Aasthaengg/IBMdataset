from collections import deque
from sys import stdin
nii=lambda:map(int,stdin.readline().split())

n=int(input())

tree=[[] for i in range(n)]
for i in range(n-1):
  u,v,w=nii()
  u-=1
  v-=1
  tree[u].append([v,w])
  tree[v].append([u,w])

ans=[-1 for i in range(n)]
ans[0]=0

que=deque()
que.append(0)

while que:
  x=que.popleft()
  for i in tree[x]:
    nx=i[0]
    nw=i[1]
    if ans[nx]==-1:
      que.append(nx)
      if nw%2==0:
        ans[nx]=ans[x]
      else:
        ans[nx]=(ans[x]+1)%2

for i in ans:
  print(i)