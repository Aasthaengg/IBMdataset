import sys
import heapq

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

INF = 10 ** 18


def warshall_floyd(V, cost):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


def main():
    N, M = in_nn()
    cost = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        cost[i][i] = 0

    edge = []
    for i in range(M):
        a, b, c = in_nn()
        a, b = a - 1, b - 1
        edge.append((min(a, b), max(a, b), c))
        cost[a][b] = c
        cost[b][a] = c

    warshall_floyd(N, cost)

    ans = set()
    for i in range(N):
        for j in range(i + 1, N):
            for e in edge:
                a, b, c = e
                if cost[i][j] == cost[i][a] + c + cost[b][j]:
                    ans.add((a, b))
                elif cost[i][j] == cost[i][b] + c + cost[a][j]:
                    ans.add((a, b))

    print(M - len(ans))


if __name__ == '__main__':
    main()
