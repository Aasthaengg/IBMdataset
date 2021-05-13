import heapq as hq
from collections import deque
N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    edges[a].append((b,1))
    edges[b].append((a,1))
INF = float("inf")
d = [INF]*N
d[0] = 0
prev = [None]*N
q = [(0,0)]
while q:
    dist, i = hq.heappop(q)
    if d[i] < dist:
        continue
    for j, w in edges[i]:
        if d[j] > d[i]+w:
            d[j] = d[i]+w
            prev[j] = i
            hq.heappush(q, (d[j], j))
path = deque()
i = N-1
while prev[i] != 0:
    path.append(prev[i])
    i = prev[i]
fncq = deque([0])
snkq = deque([N-1])
fnc = 1
snk = 1
visited = [False]*N
visited[0] = True
visited[N-1] = True
while path:
    v = path.pop()
    fncq.append(v)
    visited[v] = True
    fnc += 1
    if path:
        v = path.popleft()
        snkq.append(v)
        visited[v] = True
        snk += 1
po = [fncq, snkq]
while fncq or snkq:
    for i in range(2):
        q = po[i]
        if q:
            v = q.popleft()
            for w,_ in edges[v]:
                if not visited[w]:
                    visited[w] = True
                    q.append(w)
                    if i == 0:
                        fnc += 1
                    else:
                        snk += 1
print("Fennec" if fnc > snk else "Snuke")