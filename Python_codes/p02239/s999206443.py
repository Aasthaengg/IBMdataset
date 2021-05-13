INF = 10**18 + 7


def main():
    from collections import deque
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N):
        u, k, *A = (int(i)-1 for i in input().split())
        G[u] = A

    def bfs(s=0):
        que = deque([])
        dist = [INF]*N
        dist[s] = 0
        que.append(s)
        while que:
            pos = que.popleft()
            for v in G[pos]:
                if dist[v] != INF:
                    continue
                dist[v] = dist[pos] + 1
                que.append(v)
        return dist

    dist = bfs()
    for i, d in enumerate(dist, start=1):
        print(i, d if d != INF else -1)


if __name__ == '__main__':
    main()

