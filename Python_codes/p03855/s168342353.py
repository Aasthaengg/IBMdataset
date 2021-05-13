import sys
sys.setrecursionlimit(10 ** 6)

def find(parent, v):
    if v == parent[v]:
        return v
    parent[v] = find(parent, parent[v])
    return parent[v]

def unite(parent, rank, u, v):
    u = find(parent, u)
    v = find(parent, v)
    if u == v:
        return
    if rank[u] < rank[v]:
        parent[u] = v
    else:
        parent[v] = u
        if rank[u] == rank[v]:
            rank[u] += 1

N, K, L = map(int, input().split())
roads = list(range(N+1))
rails = list(range(N+1))
r_rank = [0] * (N + 1)
t_rank = [0] * (N + 1)

for _ in range(K):
    p, q = map(int, input().split())
    unite(roads, r_rank, p, q)
for _ in range(L):
    p, q = map(int, input().split())
    unite(rails, t_rank, p, q)

d = {}
for i in range(1, N+1):
    p = (find(roads, i), find(rails, i))
    d[p] = d.get(p, 0) + 1

print(*[d[(find(roads, i), find(rails, i))] for i in range(1, N+1)])