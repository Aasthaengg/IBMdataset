import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b = map(int, readline().split())

    print((a + b + 1) // 2)


if __name__ == '__main__':
    main()
