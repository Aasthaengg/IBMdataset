N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

def bridge(G, N):
    result = set()
    label = [None] * N
    gen = 0
    cost = [0] * N
    
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
                label[v] = gen
                gen += 1
                r = dfs(v, u)
                if r == 0:
                    result.add((u, v) if u < v else (v, u))
                res += r
        res -= cost[u]
        return res

    for v in range(N):
        if not label[v]:
            label[v] = gen
            gen += 1
            r = dfs(v, -1)
            assert r == 0, r
    return result

res = bridge(G, N)
print(len(res))
