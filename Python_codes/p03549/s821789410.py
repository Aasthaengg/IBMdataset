import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = list(map(int, readline().split()))

    timepertry = 1900 * m + 100 * (n - m)

    ans = timepertry * 2 ** m
    print(ans)


if __name__ == '__main__':
    main()
