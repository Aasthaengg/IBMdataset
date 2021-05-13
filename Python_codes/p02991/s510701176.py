N, M = [int(x) for x in input().strip().split(" ")]
from collections import deque
vs = set()
def bfs(v,d,t,N):
    queue=deque([v])
    dist = [0] * (N+1)
    while True:
        if len(queue) == 0:
            break
        v = queue.popleft()
        for u in d[v]:
            if u in vs:
                continue
            vs.add(u)
            dist[u] = dist[v] + 1
            if u == t:
                return dist[u]//3
            queue.append(u)
    return -1

d = [set() for _ in range(3*N+1)]
for _ in range(M):
    a, b = [int(x) for x in input().strip().split(" ")]
    d[a].add(N+b)
    d[N+a].add(2*N+b)
    d[2*N+a].add(b)

s, t = [int(x) for x in input().strip().split(" ")]
print(bfs(s, d, t, 3*N+1))
