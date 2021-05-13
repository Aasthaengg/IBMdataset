def solve():
    from collections import deque
    from sys import stdin
    f_i = stdin
    
    N, u, v = map(int, f_i.readline().split())
    u -= 1
    v -= 1
    adj = [[] for i in range(N)]
    for i in range(N - 1):
        A, B = map(int, f_i.readline().split())
        A -= 1
        B -= 1
        adj[A].append(B)
        adj[B].append(A)
    
    INF = 10 ** 5
    tak_dist = [INF] * N
    tak_dist[u] = 0
    aoki_dist = [INF] * N
    aoki_dist[v] = 0
    
    # BFS takahashi
    q = deque([(u, 0)])
    while q:
        pos, dist = q.popleft()
        dist += 1
        for next_pos in adj[pos]:
            if tak_dist[next_pos] > dist:
                tak_dist[next_pos] = dist
                q.append((next_pos, dist))
    
    # BFS aoki
    q = deque([(v, 0)])
    while q:
        pos, dist = q.popleft()
        dist += 1
        for next_pos in adj[pos]:
            if aoki_dist[next_pos] > dist:
                aoki_dist[next_pos] = dist
                q.append((next_pos, dist))
    
    d = (d2 for d1, d2 in zip(tak_dist, aoki_dist) if d1 < d2)
    print(max(d) - 1)

solve()