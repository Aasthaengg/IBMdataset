n, m = (int(x) for x in input().split())
LRD = [tuple(int(x) for x in input().split()) for _ in range(m)]

G = [[] for _ in range(n)]
dist = dict()
for l, r, d in LRD:
    l -= 1
    r -= 1
    G[l].append(r)
    G[r].append(l)
    dist[(l, r)] = d
    dist[(r, l)] = -d

INF = 10**18
X = [INF] * n
for i in range(n):
    stack = [i]
    while stack:
        u = stack.pop()
        if X[u] == INF:
            X[u] = 0
        for v in G[u]:  # u -> v
            if X[v] == INF:
                X[v] = X[u] + dist[(u, v)]
                stack.append(v)
            else:
                if X[v] != X[u] + dist[(u, v)]:
                    print("No")
                    exit()

print("Yes")