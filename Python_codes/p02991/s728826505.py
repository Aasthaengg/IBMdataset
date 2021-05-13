from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
S, T = map(int, input().split())
queue = deque()
queue.append((S, 0))
visited = [[False] * 3 for _ in range(N+1)]
while queue:
    u, d = queue.popleft()
    if visited[u][d % 3]:
        continue
    visited[u][d % 3] = True
    if d % 3 == 0 and u == T:
        print(d // 3)
        exit()
    for v in G[u]:
        queue.append((v, d+1))
print(-1)
