from collections import deque

N = int(input())
edges = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

# print(edges)

def bfs(v):
    dist = [N] * N
    dist[v] = 0
    q = deque()
    q.append(v)
    while q:
        p = q.popleft()
        d = dist[p]
        for e in edges[p]:
            if dist[e] == N:
                dist[e] = d + 1
                q.append(e)
    return dist

fennec = bfs(0)
snuke = bfs(N-1)

cnt = 0
for i in range(N):
    if fennec[i] <= snuke[i]:
        cnt += 1
if 2 * cnt > N:
    print('Fennec')
else:
    print('Snuke')