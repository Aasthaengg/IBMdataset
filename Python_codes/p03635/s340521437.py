import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x, y = map(int, readline().split())

    print((x - 1) * (y - 1))


if __name__ == '__main__':
    main()
