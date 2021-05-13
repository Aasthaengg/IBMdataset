def d_even_relation_bfs():
    from collections import deque
    N = int(input())
    Edges = [[int(i) for i in input().split()] for j in range(N - 1)]

    graph = [[] for _ in range(N)]
    for u, v, w in Edges:  # 頂点は 0-indexed とする
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
    distance_from_root = [0] * N  # 根は頂点 0 とする

    queue = deque([(-1, 0, 0)])  # 親と現在の頂点番号，根から親までの距離
    while queue:
        parent, current, distance = queue.pop()
        distance_from_root[current] = distance
        for next_vertex, dist in graph[current]:
            if parent != next_vertex:  # 木を「逆戻り」しない頂点だけ調べる
                queue.appendleft((current, next_vertex, distance + dist))
    ans = (1 if d % 2 == 0 else 0 for d in distance_from_root)
    return ' '.join(map(str, ans))

print(d_even_relation_bfs())