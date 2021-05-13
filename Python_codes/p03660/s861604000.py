import numpy as np
from collections import deque

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

# BFS
def dist_from_X(X:int):
    dist = np.full(N, -1)
    que = deque([X])
    dist[X] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for e in E[v]:
            if dist[e] > -1:
                continue
            dist[e] = d + 1
            que.append(e)
    return dist

Fennec = dist_from_X(0)
Sunuke = dist_from_X(N-1)

cnt = np.count_nonzero(Fennec <= Sunuke)

if cnt > N - cnt:
    print("Fennec")
else:
    print("Snuke")