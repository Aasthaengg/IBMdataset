from collections import defaultdict


N, *UVW = map(int, open(0).read().split())
g = defaultdict(set)

ans = [0] * N
for u, v, w in zip(*[iter(UVW)] * 3):
    u -= 1
    v -= 1
    g[u].add((v, w))
    g[v].add((u, w))
visited = {0}
stack = [0]
while stack:
    v = stack.pop()
    for nv, nw in g[v]:
        if nv in visited:
            continue
        if nw % 2:
            ans[nv] = ans[v] ^ 1
        else:
            ans[nv] = ans[v]
        stack.append(nv)
        visited.add(v)
print("\n".join(map(str, ans)))
