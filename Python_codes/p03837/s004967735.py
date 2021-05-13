from itertools import combinations
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
n,m = map(int,input().split())
abc = [list(map(int,input().split())) for i in range(m)]
abc = [[abc[i][0]-1,abc[i][1]-1,abc[i][2]] for i in range(m)]
graph = [[] for i in range(n+1)]
for a,b,c in abc:
  graph[a].append((b,c))
  graph[b].append((a,c))
v1,v2,edge = zip(*abc)
csr = csr_matrix((edge,(v1,v2)),shape = (n,n))
dist = floyd_warshall(csr, directed = False)
ans = 0
for i,j in combinations(range(n),2):
  fs1,fs2 = zip(*graph[i])
  if j in fs1:
    x = fs1.index(j)
    if fs2[x] > dist[i][j]:
      ans += 1
print(ans)