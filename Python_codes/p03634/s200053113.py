import sys
from collections import deque

readline = sys.stdin.readline
N = int(readline())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, readline().split())
    E[a-1].append((b-1, c))
    E[b-1].append((a-1, c))

Q, K = map(int, readline().split())
dist = [-1] * N
dist[K-1] = 0
q = deque([K-1])
while q:
    x = q.pop()
    d = dist[x]
    for i, j in E[x]:
        if dist[i] == -1:
            dist[i] = d + j
            q.append(i)
for _ in range(Q):
    x, y = map(int, readline().split())
    print(dist[x-1] + dist[y-1])
