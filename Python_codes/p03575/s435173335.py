def bridge(G, N):
    result = set()
    label = [None] * (N+1)
    gen = 0
    cost = [0] * (N+1)
    def dfs(u, p):
        nonlocal gen
        res = 0
        for v in G[u]:
            if v == p:
                continue
            if label[v] is not None:
                if label[v] < label[u]:
                    cost[v] += 1
                    res += 1
            else:
                label[v] = gen; gen += 1
                r = dfs(v, u)
                if r == 0:
                    result.add((u, v) if u < v else (v, u))
                res += r
        res -= cost[u]
        return res
    for v in range(N):
        if not label[v]:
            label[v] = gen; gen += 1
            r = dfs(v, -1)
            assert r == 0, r
    return result

from collections import deque

N,M,*abf = map(int, open(0).read().split())
ab = [abf[i*2:i*2+2] for i in range(M)]
connected = [[] for _ in range(N+1)]
ans = 0
for a, b in ab:
    connected[a].append(b)
    connected[b].append(a)
print(len(bridge(connected,N)))