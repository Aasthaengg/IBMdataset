import sys
sys.setrecursionlimit(10**4)

inf = float('inf')

# 計算量O(VE) V:頂点数, E:辺の数
# True - >正常に更新, False -> startからendまでの経路において負閉路有り
def bellmanford(start, end):
    global dist
    dist = [inf] * N
    dist[start] = 0
    # 頂点数Nなら更新は高々N-1回で済む
    for _ in range(N-1):
        for v ,nv, w in edges:
            if dist[nv] > dist[v] + w:
                dist[nv] = dist[v] + w
    # 負閉路の検出部分
    # N回目で更新があった場合、負閉路を含む
    for v, nv, w in edges:
        if dist[nv] > dist[v] + w:
            return False
    return True

def dfs(v, ad):
    visited[v] = True
    for nv in ad[v]:
        if not visited[nv]:
            dfs(nv, ad)

N, M, P = map(int,input().split())
to = [[] for _ in range(N)]
fr = [[] for _ in range(N)]
edges = []
for _ in range(M):
    A, B, C = map(int,input().split())
    A -= 1
    B -= 1
    C -= P
    C *= -1
    to[A].append(B)
    fr[B].append(A)
    edges.append((A, B, C))

visited = [False] * N

dfs(0, to)
tmp = visited[:]
visited = [False] * N
dfs(N-1, fr)
visited = [a and b for a, b in zip(tmp, visited)]
edges = [(v, nv, w) for v, nv, w in edges if visited[v] and visited[nv]]

flag = bellmanford(0, N-1)
ans = max(-dist[N-1], 0) if flag else -1
print(ans)