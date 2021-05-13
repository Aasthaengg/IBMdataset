import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, D = map(int, readline().split())

    x = 2 * D + 1

    print((N + x - 1) // x)


if __name__ == '__main__':
    main()
