INF = float('inf')
# n -> ノード数, edges -> グラフ. Vec<(start, end, cost)>で構成, s -> 始点, e -> 目的地
def bellman_ford(n, edges, s, e):
    
    # 各点への最短距離を保持する配列
    min_dist = [INF] * n

    # start地点への距離は0
    min_dist[s] = 0

    for i in range(n):
        for (start, end, cost) in edges:
            if min_dist[start] != INF and min_dist[start] + cost < min_dist[end]:
                min_dist[end] = min_dist[start] + cost
                # 最短経路の更新がn回目でもまだ行われているようなら閉路あり
                if i == n - 1 and end == n - 1:
                    return INF 
    return min_dist

n, m = map(int, input().split())
# graph -> (start, end, cost) で管理する
graph = []

for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((a - 1, b - 1, -c))

dist = bellman_ford(n, graph, 0, n - 1)
if dist == INF:
    print("inf")
else:
    print(-dist[n - 1])
