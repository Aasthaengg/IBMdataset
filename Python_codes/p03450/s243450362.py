# D - People on a Line
from collections import deque
n,m=map(int,input().split())
dist=[None]*n
edge=[[] for i in range(n)]

for i in range(m):
    l,r,d=map(int,input().split())
    edge[l-1].append((r-1,d))
    edge[r-1].append((l-1,-d))

for i in range(n):
    q=deque()
    if dist[i]==None:
        dist[i]=0
        q.append(i)
    while q:
        cur=q.popleft()
        for nx,d in edge[cur]:
            if dist[nx]==None:
                dist[nx]=dist[cur]+d
                q.append(nx)
            elif dist[nx]!=dist[cur]+d:
                print('No')
                exit()
print('Yes')