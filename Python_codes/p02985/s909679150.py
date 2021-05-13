from collections import deque
import sys
input = sys.stdin.readline

mod = 10**9+7
N, K = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visited = [False] * (N+1)
visited[1] = True
queue = deque()
queue.append(1)
ans = K
while queue:
    u = queue.popleft()
    n = K - 1 if u == 1 else K - 2
    for v in G[u]:
        if not visited[v]:
            queue.append(v)
            visited[v] = True
            ans = ans * n % mod
            n -= 1
print(ans)