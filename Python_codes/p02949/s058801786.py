from collections import deque


def bellman_ford(start: int, goal: int, graph: list) -> list:
    '''bellman-ford法: 始点startから終点goalへの最小コストを求める
    重み付きグラフgraphは隣接リストで与えられ、辺のコストは負でも良い
    次の3種類のパターンが存在する
        1. 始点startから終点goalにたどり着くことが不可能である
           -> float("inf")を返す

        2. 始点startから終点goalにたどり着くことが可能であり、
           パス上に負閉路が存在する
           -> -float("inf")を返す

        3. 始点startから終点goalにたどり着くことが可能であり、
           パス上に負閉路が存在しない
           -> 最小コストを返す

    計算量: O(|E||V|)
    '''
    INF = float("inf")
    n = len(graph)

    # スタートから到達可能な地点を調べる
    is_reachable = [False] * n
    is_reachable[start] = True
    q = deque([start])
    while q:
        pos = q.popleft()
        for next_pos, _ in graph[pos]:
            if is_reachable[next_pos]:
                continue
            is_reachable[next_pos] = True
            q.append(next_pos)

    # 逆辺で構築したグラフで、ゴールから到着可能な地点を調べる
    reverse_graph = [[] for i in range(n)]
    for pos, edge in enumerate(graph):
        for next_pos, cost in edge:
            reverse_graph[next_pos].append((pos, cost))

    is_rev_reachable = [False] * n
    is_rev_reachable[goal] = True
    q = deque([goal])
    while q:
        pos = q.popleft()
        for next_pos, _ in reverse_graph[pos]:
            if is_rev_reachable[next_pos]:
                continue
            is_rev_reachable[next_pos] = True
            q.append(next_pos)            

    is_on_the_path_from_start_to_goal = [False] * n
    for i in range(n):
        is_on_the_path_from_start_to_goal[i] = is_reachable[i] and is_rev_reachable[i]

    distance = [INF] * n
    distance[start] = 0
    for _ in range(n):
        is_updated = False
        for pos, edge in enumerate(graph):
            for next_pos, cost in edge:
                if not is_on_the_path_from_start_to_goal[next_pos]:
                    continue
                if distance[pos] != INF and distance[pos] + cost < distance[next_pos]:
                    distance[next_pos] = distance[pos] + cost
                    is_updated = True
        if not is_updated:
            return distance[goal]
    # 負閉路が存在する
    return -INF


n, m, p = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]

graph = [[] for i in range(n)]
for i in range(m):
    a, b, c = info[i]
    graph[a - 1].append((b - 1, -(c - p)))
ans = bellman_ford(0, n-1, graph)

if ans == -float("inf"):
    print(-1)
else:
    print(max(-ans, 0))