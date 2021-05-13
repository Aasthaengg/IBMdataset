import sys
sys.setrecursionlimit(10 ** 7)

N, Q = [int(_) for _ in input().split()]
edge = [[] for _ in range(N)]

for i in range(N-1):
    a, b = [int(_) for _ in input().split()]
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)


vertex = [0] * N
for i in range(Q):
    p, x = [int(_) for _ in input().split()]
    p -= 1
    vertex[p] += x


def dfs(n, parent):
    for to in edge[n]:
        if to == parent:
            continue
        vertex[to] += vertex[n]
        dfs(to, n)


dfs(0, -1)
print(*vertex)
