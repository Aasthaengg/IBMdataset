N,Q = [int(i) for i in input().split()]
graph = [[] for _ in range(N+1)]
ans = [0] * (N+1)
for i in range(N-1):
    a,b = [int(j) for j in input().split()]
    graph[a].append(b)
    graph[b].append(a)
for i in range(Q):
    pa,xaa = [int(j) for j in input().split()]
    ans[pa] += xaa

seen = [False] * (N+1)

import collections
from collections import deque
que = deque()
que.append(1)
seen[1] = True
while len(que) != 0:
    x = que.popleft()
    seta = set(graph[x])
    for i in seta:
        if seen[i]:
            continue
        ans[i] += ans[x]
        que.append(i)
        seen[i] = True
print(*ans[1:])
