from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


N = int(input())

G = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b, c = [int(_) for _ in input().split()]
    G[a].append((b, c))
    G[b].append((a, c))
Q, K = [int(_) for _ in input().split()]

# make tree
G2 = [10 ** 12] * (N + 1)

G2[K] = 0


def f():
    que = deque()
    que.append((K, 0))
    while que:
        v, p = que.pop()
        for nv, nc in G[v]:
            if nv == p: continue
            G2[nv] = G2[v] + nc
            que.append((nv, v))


f()

for i in range(Q):
    x, y = [int(_) for _ in input().split()]
    print(G2[x] + G2[y])
