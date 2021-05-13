from collections import deque
N,Q=map(int,input().split())
tree=[[] for i in range(N+1)]
counter=[0]*(N+1)
for i in range(N-1):
  a,b=map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)
for i in range(Q):
  p,x=map(int,input().split())
  counter[p]+=x
d=deque([1])
parent=[0]*(N+1)
while d:
  a=d.popleft()
  for b in tree[a]:
    if b!=parent[a]:
      counter[b]+=counter[a]
      parent[b]=a
      d.append(b)
print(*counter[1:])