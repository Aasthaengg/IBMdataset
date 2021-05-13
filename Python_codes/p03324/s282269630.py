import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    D, N = map(int, readline().split())

    if N < 100:
        print(N * 100 ** D)
    else:
        print(100 * 100 ** D + 100 ** D)


if __name__ == '__main__':
    main()
