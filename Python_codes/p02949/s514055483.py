def e_coins_respawn(N, M, P, Edges, INF=float('inf')):
    edges = [(a - 1, b - 1, P - c) for a, b, c in Edges]
    dist = [INF] * N
    dist[0] = 0

    for _ in range(N - 1):
        for u, v, w in edges:
            if dist[u] == INF:
                continue
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    ans_tmp = dist[N - 1]  # 負閉路がなければ、これが解

    # 負閉路がなければここからのループで距離は変わらない
    is_negative = [False] * N
    for _ in range(N):
        for u, v, w in edges:
            if dist[u] == INF:
                continue
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                is_negative[v] = True

            # ある頂点が負閉路の一部なら、それに隣接する頂点も負閉路の一部
            if is_negative[u]:
                is_negative[v] = True
    # 頂点Nが負閉路に含まれるなら、元のグラフでのスコアは無限大
    return -1 if is_negative[N - 1] else max(-ans_tmp, 0)

N, M, P = [int(i) for i in input().split()]
Edges = [[int(i) for i in input().split()] for j in range(M)]
print(e_coins_respawn(N, M, P, Edges))