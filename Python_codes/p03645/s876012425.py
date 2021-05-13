import sys
from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
d = [0] * N
d[0] = 1
Q = deque()
Q.append(0)
while Q:
    q = Q.popleft()
    if d[q] == 3:
        print('IMPOSSIBLE')
        sys.exit()
    for g in G[q]:
        if g == N - 1:
            print('POSSIBLE')
            sys.exit()
        if d[g] == 0:
            d[g] = d[q] + 1
            Q.append(g)
print('IMPOSSIBLE')