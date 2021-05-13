import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())

    if N % K == 0:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()
