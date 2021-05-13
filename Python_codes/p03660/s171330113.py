# G[v]: 頂点vに隣接する頂点list
# N: 頂点数
N = int(input())
from collections import defaultdict
G = defaultdict(list)
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

from collections import deque
dist = [-1]*N
que = deque([0])
dist[0] = 0
while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        que.append(w)


dist2 = [-1]*N
que = deque([N-1])
dist2[N-1] = 0
while que:
    v = que.popleft()
    d = dist2[v]
    for w in G[v]:
        if dist2[w] > -1:
            continue
        dist2[w] = d + 1
        que.append(w)

ans = [0, 0]
for a,b in zip(dist, dist2):
    if a <= b:
        ans[0] += 1
    else:
        ans[1] += 1



if ans[0] > ans[1]:
    print("Fennec")
else:
    print("Snuke")


