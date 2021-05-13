from collections import deque
N, Q = map(int, input().split())
G = [[] for _ in range(N + 1)]
c = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    c[p] += x

q = deque([1])
seen = [0] * (N + 1)
while q:
    now = q.popleft()
    seen[now] = 1
    for u in G[now]:
        if seen[u]:
            continue
        q.append(u)
        c[u] += c[now]

print(*c[1:])
