import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

n,m=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(m)]

data=np.zeros((n+1,n+1))
for u in abc:
    a,b,c=u
    data[a,b]=c
    data[b,a]=c
qqq=shortest_path(data,directed=False).astype(int)

ans=0
for u in abc:
    a,b,c=u
    if qqq[a][b]!=c:
        ans+=1
print(ans)