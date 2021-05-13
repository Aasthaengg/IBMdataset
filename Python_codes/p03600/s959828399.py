import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N = int(readline())
    G = [list(map(int, readline().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            needed = True
            for k in range(N):
                if k == i or k == j:
                    continue
                if G[i][j] > G[i][k] + G[k][j]:
                    print(-1)
                    return
                if G[i][j] == G[i][k] + G[k][j]:
                    needed = False
            if needed:
                ans += G[i][j]

    print(ans)
    return


if __name__ == '__main__':
    main()
