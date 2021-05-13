n, m = map(int, input().split())
ps = [int(i) - 1 for i in input().split()]
xy = [map(int, input().split()) for _ in range(m)]

dfind = {i: i for i in range(n)}


def find(v):
    visit = []
    while dfind[v] != v:
        visit.append(v)
        v = dfind[v]

    for i in visit:
        dfind[i] = v

    return v


def union(v0, v1):
    g0, g1 = find(v0), find(v1)
    g0, g1 = min(g0, g1), max(g0, g1)

    if g0 != g1:
        dfind[g1] = g0


for x, y in xy:
    union(x - 1, y - 1)


nmatch = 0
for i, p in enumerate(ps):
    if find(i) == find(p):
        nmatch += 1

print(nmatch)
