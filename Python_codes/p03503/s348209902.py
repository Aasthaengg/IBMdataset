import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    f = [list(map(int, readline().split())) for _ in range(n)]
    p = [list(map(int, readline().split())) for _ in range(n)]

    ans = -INF

    from itertools import product, chain

    for bit in range(1, 1 << 10):
        c = [0] * n
        for time in range(10):
            if bit >> time & 1:
                for shopnum, shopopen in enumerate(f):
                    if shopopen[time]:
                        c[shopnum] += 1

        prof = 0

        for shopnum in range(n):
            prof += p[shopnum][c[shopnum]]

        ans = max(ans, prof)

    print(ans)


if __name__ == '__main__':
    main()
