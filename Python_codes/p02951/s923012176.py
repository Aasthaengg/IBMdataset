import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B, C = map(int, readline().split())

    x = A - B

    print(max(0, C - x))


if __name__ == '__main__':
    main()
