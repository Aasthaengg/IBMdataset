import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b = map(int, readline().split())

    x = b - a
    y = x * (x - 1) // 2

    print(y - a)


if __name__ == '__main__':
    main()
