from collections import deque
from sys import stdin
nii=lambda:map(int,stdin.readline().split())

n=int(input())

tree=[[] for i in range(n)]
for i in range(n-1):
  a,b,c=nii()
  a-=1
  b-=1
  tree[a].append([b,c])
  tree[b].append([a,c])

q,k=nii()
k-=1

dist=[-1 for i in range(n)]
dist[k]=0

que=deque()
que.append(k)

while que:
  x=que.popleft()
  for tb,tc in tree[x]:
    if dist[tb]==-1:
      que.append(tb)
      dist[tb]=dist[x]+tc

for i in range(q):
  x,y=nii()
  x-=1
  y-=1
  print(dist[x]+dist[y])