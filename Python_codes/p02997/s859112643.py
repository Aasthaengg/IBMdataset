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


INF = 10 * 5


def warshall_floyd(V, cost):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


def main():

    N, K = in_nn()

    G = [[INF] * N for _ in range(N)]
    ans = []

    for i in range(1, N):
        G[0][i] = 1
        G[i][0] = 1
        ans.append((1, i + 1))

    warshall_floyd(N, G)

    comb = []
    for i in range(N):
        for j in range(i + 1, N):
            if G[i][j] == 2:
                comb.append((i + 1, j + 1))

    comb = deque(comb)
    max_k = len(comb)

    if max_k < K:
        print(-1)
        exit()

    while max_k > K:
        max_k -= 1
        ans.append(comb.popleft())

    print(len(ans))
    for i, j in ans:
        print(i, j)


if __name__ == '__main__':
    main()
