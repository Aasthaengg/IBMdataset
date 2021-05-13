import sys
sys.setrecursionlimit(10 ** 5)


def main():
    def DFS(v):
        if DP[v] == -1:
            res = 0
            for i in G[v]:
                res = max(res, DFS(i) + 1)

            DP[v] = res

        return DP[v]


    N, M = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(M)]

    G = [[] for _ in range(N)]
    for x, y in xy:
        G[x - 1].append(y - 1)

    DP = [-1] * N
    for v in range(N):
        DFS(v)

    print(max(DP))


if __name__ == '__main__':
    main()

exit()
