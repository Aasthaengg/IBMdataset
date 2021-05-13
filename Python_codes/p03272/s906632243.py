import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, x = map(int, readline().split())

    print(N - x + 1)


if __name__ == '__main__':
    main()
