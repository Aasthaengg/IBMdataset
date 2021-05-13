from collections import deque

n,k = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n-1)]
tree = [list() for i in range(n+1)]
visited = [0] * (n+1)
for a,b in ab:
  tree[a].append(b)
  tree[b].append(a)
visited[1] = 1
queue = deque([(1,0)])
ans = k
mod = 10 ** 9 + 7
while queue:
  vertex, depth = queue.popleft()
  res = k - min(depth+1,2)
  for NEXT in tree[vertex]:
    if not visited[NEXT]:
      visited[NEXT] = 1
      ans *= res
      ans %= mod
      res -= 1
      queue.append((NEXT,depth+1))
print(ans)