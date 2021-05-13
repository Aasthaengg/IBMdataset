from collections import deque
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

count = [0] * N
for j in range(Q):
    p, x = map(int, input().split())
    count[p-1] += x

visited = [False] * N
que = deque([0])

while que:
    now = que.pop()
    visited[now] = True
    for nxt in G[now]:
        if visited[nxt]:
            continue
        count[nxt] += count[now]
        que.appendleft(nxt)

print(*count)
