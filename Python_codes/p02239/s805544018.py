from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N):
    ls = list(map(int, input().split()))
    u = ls[0] - 1
    for v in ls[2:]:
        G[u].append(v - 1)

dist = [-1] * N
que = deque([0])
dist[0] = 0

while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        que.append(w)

for v in range(N):
    print("{} {}".format(v + 1, dist[v]))
