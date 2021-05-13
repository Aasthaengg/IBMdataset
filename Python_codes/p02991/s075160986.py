from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
G = [[] for i in range(3 * N)]
for i in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    G[3 * u + 0].append(3 * v + 1)
    G[3 * u + 1].append(3 * v + 2)
    G[3 * u + 2].append(3 * v + 0)
S, T = map(int, input().split())
S, T = S - 1, T - 1
INF = float('inf')
d = [INF] * (3 * N)
d[3 * S] = 0


que = deque([3 * S])
while que:
    u = que.popleft()
    for w in G[u]:
        if d[w] == INF:
            d[w] = d[u] + 1
            que.append(w)


ans = d[3 * T]
if ans == INF:
    print(-1)
else:
    print(ans // 3)