import sys
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def topological_sort(N, dag):

    degree = [0] * N
    for i in range(N):
        for v in dag[i]:
            degree[v] += 1

    ret = [v for v in range(N) if degree[v] == 0]
    q = deque(ret)

    while q:
        v = q.popleft()
        for nv in dag[v]:
            degree[nv] -= 1
            if degree[nv] == 0:
                q.append(nv)
                ret.append(nv)

    return ret


def main():

    N, M = in_nn()

    edge = [[] for _ in range(N)]
    for i in range(M):
        x, y = in_nn()
        x, y = x - 1, y - 1
        edge[x].append(y)

    dp = [0] * N
    vs = topological_sort(N, edge)
    for v in vs:
        for nv in edge[v]:
            dp[nv] = max(dp[nv], dp[v] + 1)

    print(max(dp))


if __name__ == '__main__':
    main()
