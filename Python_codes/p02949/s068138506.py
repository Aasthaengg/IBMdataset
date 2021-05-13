import collections
N, M, P = [int(_) for _ in input().split()]
ABC = [[int(_) for _ in input().split()] for _ in range(M)]
cd = collections.defaultdict
Ga = cd(set)
Gb = cd(set)
G = []
ok = cd(int)
for a, b, c in ABC:
    Ga[a].add(b)
    Gb[b].add(a)
#dfs
for pair in [[1, Ga], [N, Gb]]:
    S = pair
    Gn = pair.pop()
    visited = [0] * (N + 1)
    while S:
        s = S.pop()
        if not visited[s]:
            visited[s] = 1
            ok[s] += 1
            for ns in Gn[s]:
                S += [ns]
for a, b, c in ABC:
    if ok[a] == ok[b] == 2:
        G += [(a, b, P - c)]


def bellman_ford(V, G, i):
    INF = float('inf')
    D = [INF] * V
    D[i] = 0
    for _ in range(V):
        update = False
        for s, t, d in G:
            if D[s] != INF and D[t] > D[s] + d:
                D[t] = D[s] + d
                update = True
        if not update:
            return D
        if _ == V:
            return False


a = bellman_ford(N + 1, G, 1)
try:
    print(max(-a[-1], 0))
except:
    print(-1)
