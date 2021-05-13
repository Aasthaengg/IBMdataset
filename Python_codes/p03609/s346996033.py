import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x, t = map(int, readline().split())

    print(max(0, x - t))


if __name__ == '__main__':
    main()
