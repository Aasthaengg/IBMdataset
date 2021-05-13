import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, a, b = map(int, readline().split())

    if (b - a - 1) % 2 == 0:
        print("Borys")
    else:
        print("Alice")


if __name__ == '__main__':
    main()
