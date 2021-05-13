from sys import stdin

def find(parent, i):
  if parent[i] == i:
    return i
  parent[i] = find(parent, parent[i])
  return parent[i]

def unite(parent, i, j):
  i = find(parent, i)
  j = find(parent, j)
  if i == j:
    return
  parent[i] = j

n, k, l = map(int, stdin.readline().split())

roads = list(range(n))
rails = list(range(n))

for i in range(k):
  p, q = map(int, stdin.readline().split())
  unite(roads, p - 1, q - 1)

for i in range(l):
  p, q = map(int, stdin.readline().split())
  unite(rails, p - 1, q - 1)

d = {}
for i in range(n):
  t = (find(roads, i), find(rails, i))
  if t in d:
    d[t] += 1
  else:
    d[t] = 1

print(*[d[(find(roads, i), find(rails, i))] for i in range(n)])
