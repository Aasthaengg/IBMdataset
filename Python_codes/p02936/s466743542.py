import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
G = [[] for _ in [0]*N]
for _ in [0]*(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

add = [0]*N
for _ in [0]*M:
    p, x = map(int, input().split())
    p -= 1
    add[p] += x
counter = [0]*N


def dfs(v, p, x):
    counter[v] = x
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v, x+add[u])


dfs(0, -1, add[0])

print(*counter)
