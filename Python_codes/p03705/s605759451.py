import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, a, b = map(int, readline().split())
    ans = max(b * (n - 2) - a * (n - 2) + 1, 0)
    print(ans)


if __name__ == '__main__':
    main()
