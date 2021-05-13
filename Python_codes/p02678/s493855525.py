
from collections import deque

N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
for a, b in X:
    graph[a].append(b)
    graph[b].append(a)

INF = 10 ** 9 + 7
d = [INF] * (N + 1)
ans = [0] * (N + 1)
q = deque([1])
d[1] = 0
while q:
    u = q.popleft()
    for v in graph[u]:
        if d[v] > d[u] + 1:
            d[v] = d[u] + 1
            ans[v] = u
            q.append(v)

print("Yes")
print(*ans[2:], sep="\n")
