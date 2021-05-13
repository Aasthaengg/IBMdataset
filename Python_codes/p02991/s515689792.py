from collections import deque
N, M = map(int, input().split())
G = [[[] for j in range(3)] for i in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    for i in range(3):
        G[u][i].append((v, (i+1) % 3))
S, T = map(int, input().split())


visited = [[-1] * 3 for _ in range(N+1)]

que = deque([(S, 0, 0)])
visited[S][0] = 0

while que:
    ci, l, d = que.popleft()

    for ni, nl in G[ci][l]:
        if visited[ni][nl] == -1:
            que.append((ni, nl, d+1))
            visited[ni][nl] = d+1

print(visited[T][0]//3)
