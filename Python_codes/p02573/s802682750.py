N, M = map(int, input().split())
r = [i for i in range(N+1)]
n = [0 for i in range(N+1)]
buf = []

def root(x):
  if x==r[x]:
    return x
  else:
    r[x] = root(r[x])
    return r[x]

def unite(x, y):
  rx = root(x)
  ry = root(y)
  if rx < ry:
    r[ry] = rx
  elif rx > ry:
    r[rx] = ry
    

for _ in range(M):
  a, b = map(int, input().split())
  unite(a, b)

for x in range(1, N+1):
  if r[x] != x and r[r[x]] != r[x]:
    _ = root(x)
  
  
for x in r[1:]:
  n[x] += 1
    
ans = max(n[1:])

print(ans)