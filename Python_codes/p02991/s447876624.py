import sys
from collections import deque


data = sys.stdin.readlines()
N, M = map(int, data[0].split())
edge = [[] for _ in range(N)]
for i in range(1, M + 1):
    u, v = map(int, data[i].split())
    u -= 1
    v -= 1
    edge[u].append(v)
S, T = map(lambda x: int(x) - 1, data[M + 1].split())

visited = set()
q = deque()
q.append((0, S))
ans = 10 ** 10
while len(q) > 0:
    c, v = q.popleft()
    key = (c % 3, v)
    if key in visited:
        continue
    visited.add(key)
    if v == T and c % 3 == 0:
        ans = min(ans, c // 3)
    else:
        for e in edge[v]:
            newKey = (c + 1, e)
            q.append(newKey)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)
