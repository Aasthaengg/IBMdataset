import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *LRD = map(int, read().split())

    G = [[] for _ in range(N)]
    for l, r, d in zip(*[iter(LRD)] * 3):
        G[l - 1].append((r - 1, d))
        G[r - 1].append((l - 1, -d))

    seen = [False] * N
    dist = [-1] * N
    for i in range(N):
        if seen[i]:
            continue

        dist[i] = 0
        queue = deque([i])
        while queue:
            v = queue.popleft()
            for nv, d in G[v]:
                if seen[nv]:
                    if dist[nv] != dist[v] + d:
                        print('No')
                        return
                else:
                    dist[nv] = dist[v] + d
                    seen[nv] = True
                    queue.append(nv)

    print('Yes')
    return


if __name__ == '__main__':
    main()
