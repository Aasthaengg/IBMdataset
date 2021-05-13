import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, x = map(int, readline().split())

    print(b // x - (a - 1) // x)


if __name__ == '__main__':
    main()
