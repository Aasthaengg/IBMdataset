from collections import deque

mod = 10 ** 9 + 7

N, K, *AB = map(int, open(0).read().split())

E = [[] for _ in range(N + 1)]
for a, b in zip(*[iter(AB)] * 2):
    E[a].append(b)
    E[b].append(a)

ans = K
visited = [False] * (N + 1)
Q = deque([1])
while Q:
    v = Q.popleft()
    visited[v] = True

    k = K - 2 if v != 1 else K - 1
    for u in E[v]:
        if visited[u]:
            continue
        Q.append(u)
        ans = (ans * k) % mod
        k -= 1

print(ans)
