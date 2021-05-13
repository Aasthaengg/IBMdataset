from collections import deque

N = int(input())
tree = [[] for i in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  a -= 1; b -= 1
  tree[a].append(b); tree[b].append(a)

C = list(map(int, input().split()))
C.sort()
ans = sum(C[:-1])
dep = [-1] * N
dep[0] = C.pop()
d = deque([[0, -1]])
while d:
  node, par = d.popleft()
  children = tree[node]
  for child in children:
    if child == par:
      continue
    dep[child] = C.pop()
    d.append([child, node])

print(ans)
print(*dep)