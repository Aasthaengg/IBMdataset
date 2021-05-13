import sys
N, M, P = map(int, input().split())
Edge = []
G = [[] for i in range(N)]
G_rev = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    a, b = a - 1, b - 1
    c = -(c - P)
    Edge.append([a, b, c])
    G[a].append(b)
    G_rev[b].append(a)


# 0とNの両方から辿れない頂点を削除
def dfs(g, stack):
    can_reach = set()
    while stack:
        n = stack.pop()
        can_reach.add(n)
        for to in g[n]:
            if to in can_reach:
                continue
            stack.append(to)
    return can_reach


can_reach_from_0 = dfs(G, [0])
can_reach_from_N = dfs(G_rev, [N - 1])

can_reach_from_0_and_N = can_reach_from_0 & can_reach_from_N
EdgeShifted = []
for a, b, c in Edge:
    if (a in can_reach_from_0_and_N) and (b in can_reach_from_0_and_N):
        EdgeShifted.append([a, b, c])


# ベルマンフォード
dist = [float('inf')] * N
dist[0] = 0

for n in range(len(can_reach_from_0_and_N)):
    for fr, to, cost in EdgeShifted:
        if dist[to] > dist[fr] + cost:
            dist[to] = dist[fr] + cost
            # 負閉路検出
            if n == len(can_reach_from_0_and_N) - 1:
                print(-1)
                exit()

print(max(0, -dist[N - 1]))
