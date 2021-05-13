import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())

    for i in range(1, n + 1):
        min_lim = (i - 1) * i // 2 + 1
        max_lim = i * (i + 1) // 2
        if min_lim <= n <= max_lim:
            print(i)
            sys.exit()


if __name__ == '__main__':
    main()
