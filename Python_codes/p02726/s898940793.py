import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, X, Y = map(int, readline().split())

    X -= 1
    Y -= 1

    G = [[] for _ in range(N)]
    for i in range(N - 1):
        G[i].append(i + 1)
        G[i + 1].append(i)

    G[X].append(Y)
    G[Y].append(X)

    count = [0] * N

    for i in range(N):
        dist = [-1] * N
        dist[i] = 0
        queue = deque([i])
        while queue:
            v = queue.popleft()
            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    count[dist[nv]] += 1
                    queue.append(nv)

    ans = [c // 2 for c in count[1:]]
    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()
