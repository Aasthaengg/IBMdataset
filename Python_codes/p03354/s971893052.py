N, M = map(int, input().split())
par = [i for i in range(N)]
rank = [0 for _ in range(N)]

def root(x):
  if par[x] == x:
    return x
  else:
    par[x] = root(par[x])
    return par[x]
def unite(x, y):
  s, t = root(x), root(y)
  if s != t:
    if rank[s] < rank[t]:
      par[s] = t
    else:
      par[t] = s
      if rank[s] == rank[t]:
        rank[s] += 1
        
p = list(map(int, input().split()))
for i in range(N):
  p[i] -= 1
for i in range(M):
  x, y = map(int, input().split())
  unite(x-1, y-1)
for i in range(N):
  par[i] = root(i)
cnt = 0
for i in range(N):
  if par[i] == par[p[i]]:
    cnt += 1
print(cnt)