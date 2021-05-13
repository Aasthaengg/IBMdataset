def d_fennec_vs_snuke():
    from collections import deque
    N = int(input())
    Edges = [[int(i) for i in input().split()] for j in range(N - 1)]

    graph = [[] for _ in range(N)]
    for a, b in Edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    def bfs(start, tree_size=N, tree=graph):
        """木のある頂点 start からの距離を求める (start は 0-origin)"""
        dist = [0] * tree_size
        is_visited = [False] * tree_size
        is_visited[start] = True

        queue = deque([start])
        while queue:
            current = queue.pop()
            for child in tree[current]:
                if is_visited[child]:
                    continue
                is_visited[child] = True
                dist[child] = dist[current] + 1
                queue.appendleft(child)
        return dist

    fennec_dist, snuke_dist = bfs(0), bfs(N - 1)
    fennec_point, snuke_point = 0, 0  # 各々が色を塗れたマスの数

    for fennec, snuke in zip(fennec_dist, snuke_dist):
        if fennec <= snuke:
            fennec_point += 1
        else:
            snuke_point += 1
    return 'Fennec' if fennec_point > snuke_point else 'Snuke'

print(d_fennec_vs_snuke())