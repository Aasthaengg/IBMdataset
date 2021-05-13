n,q=map(int,input().split())
cnt=[0]*(n)
g=[[] for _ in range(n)]
for _ in range(n-1): #木グラフの隣接リストを作成
  a,b=map(int,input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)
for _ in range(q):
    a , b = map(int,input().split())
    a = a - 1
    cnt[a] += b
import collections
q=collections.deque()
q.append(0)
check=[0]*n
while q:
  v=q.popleft()
  check[v]=1
  for u in g[v]:
    if check[u]==1:
      continue
    cnt[u]+=cnt[v]
    q.append(u)
print(*cnt)