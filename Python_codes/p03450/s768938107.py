from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    l, r, d = map(int, input().split())
    graph[l - 1].append([r - 1, d])
    graph[r - 1].append([l - 1, -d])
X = [None] * N


def bfs(u):
    que = deque([(u, 0)])
    X[u] = 0
    while que:
        u, x = que.popleft()
        for nu, add in graph[u]:
            nx = x + add
            if X[nu] == nx:
                continue
            if X[nu] is not None and X[nu] != nx:
                print('No')
                exit()
            X[nu] = nx
            que.append((nu, nx))


for i in range(N):
    if X[i] is None:
        bfs(i)
print('Yes')
