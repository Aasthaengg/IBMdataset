import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = map(int, readline().split())
    if 2 * n > m:
        ans = min(n, m // 2)
    else:
        c = m - 2 * n
        ans = n + c // 4

    print(ans)


if __name__ == '__main__':
    main()
