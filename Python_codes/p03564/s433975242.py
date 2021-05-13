import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    K = int(readline())

    cur = 1

    for _ in range(N):
        cur = min(2 * cur, cur + K)

    print(cur)


if __name__ == '__main__':
    main()
