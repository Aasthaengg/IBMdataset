n, q = map(int, input().split())
tree = [[] for _ in range(n)]
point = [0] * n
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

for _ in range(q):
    p, x = map(int, input().split())
    point[p-1] += x

stack = [[0, 0, -1]]
while stack:
  v, p, parent = stack.pop()
  point[v] += p
  for child in tree[v]:
    if child == parent:
      continue
    stack.append([child,point[v],v])

print(*point)