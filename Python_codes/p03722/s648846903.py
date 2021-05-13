inf = float('inf')
# ベルマンフォード法
# 計算量O(VE) V:頂点数, E:辺の数
# [引数]   n:頂点数, edges:辺集合, start:始点, end:終点
# [返り値] dist:startからの最短距離, exists_negative_cycle: 負閉路が存在するかどうか
def bellmanford(n : int, edges : list, start : int, goal : int) -> (list, bool):
    dist = [inf] * n
    dist[start] = 0
    exist_negative_cycle = True

    # 負閉路を含まないとき、頂点数nなら更新は高々n-1回で済む
    for _ in range(N-1):
        for v, nv, w in edges:
            if dist[nv] > dist[v] + w:
                dist[nv] = dist[v] + w


    # (1)グラフに負閉路が含まれるときの検出
    # N回目で更新があったとき、グラフは負閉路を含む
    # for v, nv, w in edges:
    #     if dist[nv] > dist[v] + w:
    #         is_cycle = False

    # (2)startとendのパスに負閉路が含まれるときの検出
    is_updated = [False] * n
    for _ in range(N):
        for v, nv, w in edges:
            if dist[nv] > dist[v] + w:
                dist[nv] = dist[v] + w
                is_updated[nv] = True
            if is_updated[v] is True:
                is_updated[nv] = True

    exist_negative_cycle = is_updated[goal]

    return dist, exist_negative_cycle

N, M = map(int,input().split())
edges = []
for _ in range(M):
    a, b, c = map(int,input().split())
    a -= 1; b -= 1
    edges.append((a, b, -c))

dist, exist_negative_cycle = bellmanford(N, edges, 0, N-1)

if exist_negative_cycle is True:
    ans = "inf"
else:
    ans = -dist[N-1]

print(ans)