import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N = int(readline())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, readline().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    dist = [-1] * N
    color = [0] * N
    dist[0] = 0
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for nv, cost in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + cost
                color[nv] = dist[nv] % 2
                queue.append(nv)

    print(*color, sep='\n')
    return


if __name__ == '__main__':
    main()
