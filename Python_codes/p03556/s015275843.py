import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    i = 0
    while (i + 1) ** 2 <= N:
        i += 1
    print(i ** 2)


if __name__ == '__main__':
    main()
