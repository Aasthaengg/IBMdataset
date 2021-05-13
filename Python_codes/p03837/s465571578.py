import heapq


def dijkstra(adj, start, goal=None):
    num = len(adj)          # グラフのノード数
    dist = [float('inf') for i in range(num)]  # 始点から各頂点までの最短距離を格納する
    prev = [float('inf') for i in range(num)]  # 最短経路における，その頂点の前の頂点のIDを格納する

    dist[start] = 0
    # プライオリティキュー．各要素は，(startからある頂点vまでの仮の距離, 頂点vのID)からなるタプル
    q = []
    heapq.heappush(q, (0, start))  # 始点をpush

    while q:
        prov_cost, src = heapq.heappop(q)  # pop

        # プライオリティキューに格納されている最短距離が，現在計算できている最短距離より大きければ，distの更新をする必要はない
        if dist[src] < prov_cost:
            continue

        # 他の頂点の探索
        for dest in range(num):
            cost = adj[src][dest]
            if cost != float('inf') and dist[dest] > dist[src] + cost:
                dist[dest] = dist[src] + cost  # distの更新
                # キューに新たな仮の距離の情報をpush
                heapq.heappush(q, (dist[dest], dest))
                prev[dest] = src                      # 前の頂点を記録

    return dist


n, m = map(int, input().split())
mat = [[float('inf')] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    mat[a - 1][b - 1] = c
    mat[b - 1][a - 1] = c
for i in range(n):
    mat[i][i] = 0
mat2 = []
for i in range(n):
    mat2.append(dijkstra(mat, i))
ans = 0
for i in range(n):
    for j in range(i, n):
        if mat[i][j] != float('inf') and mat[i][j] != mat2[i][j]:
            ans += 1
print(ans)