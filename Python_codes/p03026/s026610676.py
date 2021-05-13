from collections import deque
n=int(input())
g=[set() for i in range(n+1)]
for i in range(n-1):
  a,b=map(int,input().split())
  g[a].add(b)
  g[b].add(a)
c=list(map(int,input().split()))
c.sort(reverse=True)
print(sum(c)-c[0])
q=deque()
nums=[0]*(n+1)
q.appendleft(1)
while q:
  d=q.popleft()
  nums[d]=c.pop(0)
  for node in g[d]:
    if nums[node]==0:
      q.append(node)
print(*nums[1:])