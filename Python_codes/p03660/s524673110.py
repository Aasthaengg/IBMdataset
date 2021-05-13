import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)


def dfs(v, dist):
    for u in G[v]:
        if dist[u] != -1:
            continue
        dist[u] = dist[v] + 1
        ret = dfs(u, dist)


dist_fen = [-1] * N
dist_fen[0] = 0
dfs(0, dist_fen)

dist_snu = [-1] * N
dist_snu[N-1] = 0
dfs(N-1, dist_snu)

fen = 0
for v in range(N):
    if dist_fen[v] <= dist_snu[v]:
        fen += 1
if fen > N // 2:
    print('Fennec')
else:
    print('Snuke')
