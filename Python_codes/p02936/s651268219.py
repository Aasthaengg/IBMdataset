
from collections import deque


from collections import deque

N, Q = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N - 1)]
Y = [list(map(int, input().split())) for _ in range(Q)]

tree =[[] for _ in range(N + 1)]
for a, b in X:
    tree[a].append(b)
    tree[b].append(a)

ctr = [0] * (N + 1)
for p, x in Y:
    ctr[p] += x

ans = [0] * (N + 1)
ans[1] = ctr[1]
visited = [False] * (N + 1)
visited[1] = True
q = deque([1])
while q:
    u = q.popleft()
    for v in tree[u]:
        if not visited[v]:
            ans[v] = ans[u] + ctr[v]
            visited[v] = True
            q.append(v)

print(*ans[1:])
