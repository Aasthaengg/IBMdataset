def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    # adj = [[], [(to, cost), (to, cost), ...], [(to, cost), (to, cost), ...], ...]
    def BellmanFord(adj, start):
        N = len(adj) - 1
        inf = 10**13
        dist = [inf] * (N + 1)
        dist[start] = 0
        neg_loop_flg = 0
        for i in range(N):
            updated = 0
            for fr in range(1, N + 1):
                if dist[fr] == inf:
                    continue
                for to, cost in adj[fr]:
                    if dist[fr] + cost < dist[to]:
                        dist[to] = dist[fr] + cost
                        updated = 1
            if not updated:
                break
            if i == N - 1:
                if updated:
                    neg_loop_flg = 1

        return dist, neg_loop_flg

    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[b].append((a, -c))

    adj_new = [[] for _ in range(N+1)]
    que = deque()
    que.append(N)
    seen = [0] * (N+1)
    seen[N] = 1
    while que:
        v = que.pop()
        for u, cost in adj[v]:
            if not seen[u]:
                seen[u] = 1
                que.append(u)
            adj_new[u].append((v, cost))

    dist, flg = BellmanFord(adj_new, 1)
    if flg:
        print('inf')
    else:
        print(-dist[N])


if __name__ == '__main__':
    main()
