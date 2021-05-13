import sys
from collections import deque
n,m = map(int, sys.stdin.readline().rstrip("\n").split())
edge = [[] for i in range(n)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().rstrip("\n").split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
footprint = [10**9+7]*n
q = deque()
footprint[0] = 0
for i in edge[0]:
    q.append((i,0))
while q:
    nn,fn = q.popleft()
    if footprint[nn] == 10**9+7:
        footprint[nn] = fn
        for i in edge[nn]:
            if footprint[i] == 10**9+7:
                q.append((i,nn))
if 10**9+7 in footprint:
    print('No')
else:
    print('Yes')
    for i in range(1,n):
        print(footprint[i]+1)