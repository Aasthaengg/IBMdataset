import sys


def input():
    return sys.stdin.readline().strip()


MOD = 10 ** 9 + 7
sys.setrecursionlimit(20000000)
INF = float("inf")


def main():
    n, m, d = map(int, input().split())
    if d == 0:
        print(n * (m - 1) / (n ** 2))
    else:
        print((n - d) * 2 * (m - 1) / (n ** 2))


if __name__ == "__main__":
    main()
