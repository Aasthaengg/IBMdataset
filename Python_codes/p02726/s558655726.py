#!/usr/bin/env python3
def main():
    from collections import deque
        
    N, X, Y = map(int, input().split())

    G = [[1]] + [[x - 1, x + 1] for x in range(1, N - 1)] + [[N - 2]]
    G[X - 1].append(Y - 1)
    G[Y - 1].append(X - 1)

    dist = [[-1] * N for _ in [0] * N]
    for start in range(N):
        q = deque([start])
        dist[start][start] = 0
        while q:
            now = q.popleft()
            for next in G[now]:
                if dist[start][next] == -1:
                    dist[start][next] = dist[start][now] + 1
                    q.append(next)
    res = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            res[dist[i][j]] += 1
    for d in range(1, N):
        print(res[d])


if __name__ == '__main__':
    main()
