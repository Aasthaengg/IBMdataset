n, m = map(int, input().split())
p = list(map(lambda x: int(x)-1, input().split()))
q = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

par = [x for x in range(n)]
rank = [0]*n

def find(x):
  if par[x] == x:
    return x
  else:
    par[x] = find(par[x])
    return par[x]

def unite(x, y):
  x = find(x)
  y = find(y)
  if x == y: return
  if rank[x] < rank[y]:
    par[x] = y
  else:
    par[y] = x
    if rank[x] == rank[y]: rank[x] += 1

def same(x, y):
  return find(x) == find(y)

for x, y in q:
  unite(x, y)
#print(par)
#print(rank)
ans = 0
for i in range(n):
  if same(p[i], i): ans += 1
print(ans)