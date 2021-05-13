import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B, C, D = map(int, readline().split())

    print(max(A * B, C * D))


if __name__ == '__main__':
    main()
