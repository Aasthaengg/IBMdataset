import sys

readline = sys.stdin.buffer.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m, q = map(int, readline().split())
    cum = [[0] * 502 for _ in range(502)]

    for _ in range(m):
        l, r = map(int, readline().split())
        cum[l][r] += 1

    ans = [[0] * 502 for _ in range(502)]

    for i in range(1, 501):
        for j in range(1, 501):
            ans[i][j] = ans[i][j - 1] + cum[i][j]

    for i in range(500, 0, -1):
        for j in range(1, 501):
            ans[i][j] += ans[i + 1][j]

    for _ in range(q):
        l, r = map(int, readline().split())
        print(ans[l][r])


if __name__ == '__main__':
    main()
