from collections import deque
n,q=map(int,input().split())
tree=[deque([]) for _ in range(n+1)]
for i in range(n-1):
  a,b=map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)
ans=[0]*(n+1)
for i in range(q):
  p,x=map(int,input().split())
  ans[p]+=x
seen=[0]*(n+1)
stack=[]
def dfs():
  stack.append(1)
  seen[1]=1
  while stack:
    s=stack.pop()
    if not tree[s]:
      continue
    for j in range(len(tree[s])):
      g_NO = tree[s].popleft()
      if seen[g_NO]:
        continue
      seen[g_NO] = 1
      stack.append(g_NO)
      ans[g_NO] += ans[s]


dfs()
print(*ans[1:])

