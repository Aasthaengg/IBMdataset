import sys
from collections import deque
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    G = [[] for i in range(N)]
    for i in range(N - 1):
        a, b, c = map(int, readline().split())
        G[a-1].append((b-1, c))
        G[b-1].append((a-1, c))

    dist = [-1 for i in range(N)]
    Q, K = map(int, readline().split())
    dist[K-1] = 0
    q = deque([[K - 1, 0, -1]])
    while q:
        v, d, parent = q.popleft()
        dist[v] = d
        for child in G[v]:
            if child[0] == parent:
                continue
            q.append([child[0], d + child[1], v])

    for i in range(Q):
        x, y = map(int, readline().split())
        print(dist[x - 1] + dist[y - 1])


if __name__ == '__main__':
    main()