import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    A = list(map(int, readline().split()))

    s = 0

    for x in A:
        s += 1 / x

    print(1 / s)


if __name__ == '__main__':
    main()
