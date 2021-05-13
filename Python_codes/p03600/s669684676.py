import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N = int(readline())
    G = [list(map(int, readline().split())) for _ in range(N)]

    H = [[True] * N for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(i + 1, N):
                if G[i][j] > G[i][k] + G[k][j]:
                    print(-1)
                    return
                if k not in (i, j) and G[i][j] == G[i][k] + G[k][j]:
                    H[i][j] = False

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if H[i][j]:
                ans += G[i][j]

    print(ans)
    return


if __name__ == '__main__':
    main()
