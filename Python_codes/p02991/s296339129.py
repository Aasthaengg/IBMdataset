import queue
N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)

S, T = map(int, input().split())
S -= 1
T -= 1

INF = 1001001001
dist = [[0] * 3 for _ in range(100005)]

for i in range(N):
    for j in range(3):
        dist[i][j] = INF

q = queue.Queue()
q.put((S, 0))
dist[S][0] = 0
while not q.empty():
    e = q.get()
    v = e[0]
    l = e[1]
    for u in edges[v]:
        nl = (l + 1) % 3
        if dist[u][nl] != INF:
            continue
        dist[u][nl] = dist[v][l] + 1
        q.put((u, nl))

ans = dist[T][0]
if ans == INF:
    ans = -1
else:
    ans //= 3
print(ans)