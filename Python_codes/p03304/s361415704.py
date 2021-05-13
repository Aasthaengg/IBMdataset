import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m, d = map(int, readline().split())

    if d == 0:
        x = 1 / n * (m - 1)
    else:
        x = max(0, n - d) * (1 / n ** 2) + (n - d) * (1 / n ** 2)
        x *= (m - 1)

    print(x)


if __name__ == '__main__':
    main()
