import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
tree=[[] for _ in range(N)]
for _ in range(N-1):
  u,v,w=map(int,input().split())
  tree[u-1].append((v-1,w))
  tree[v-1].append((u-1,w))
ans=[-1]*N
ans[0]=0
d=deque([0])
while d:
  p=deque.popleft(d)
  color=ans[p]
  for v,w in tree[p]:
    if ans[v]==-1:
      deque.append(d,v)
      ans[v]=color^(w%2)
print(*ans,sep='\n')