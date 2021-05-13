import sys
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
Graph = [[] for i in range(n)]
seen = [False]*n
point = [0]*n


def dfs(g, v, p):
    # vを訪問済みにする
    seen[v] = True
    if p != -1: point[v] += point[p]

    # vから行ける各頂点について
    for next_v in g[v]:

        # next_vが訪問済みだったらスルー
        if seen[next_v]: continue

        # 再帰的に探索
        dfs(g, next_v, v)


for i in range(n-1):
    a, b = map(int, input().split())
    a-=1
    b-=1

    # 無向グラフを想定
    Graph[a].append(b)
    Graph[b].append(a)


for i in range(q):
    x, p = map(int, input().split())
    point[x-1] += p


dfs(Graph, 0, -1)


print(*point)
