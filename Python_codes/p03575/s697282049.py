from collections import deque

def Graph(ab):
    G = [[] for i in range(n)]
    for a,b in ab:
        G[a-1].append(b)
        G[b-1].append(a)
    return G

def dfs(G, a, b):
    #(a, b)は除外する辺
    q = deque()
    q.append((1,-1))
    log = [0] * n
    log[0] = 1
    while q:
        V, P = q.pop()
        for new_v in G[V-1]:
            if {a, b} == {new_v, V}:#除外する辺であれば
                continue
            if new_v == P:#戻らない
                continue
            if log[new_v - 1]:#過去に行った頃がある点に行かない。
                continue
            log[new_v - 1] = 1
            q.append((new_v,V))
    return sum(log) != n

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
G = Graph(ab)

ans = 0
for a, b in ab:
    if dfs(G, a, b):
        ans += 1
print(ans)