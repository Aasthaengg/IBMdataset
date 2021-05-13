import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    cur = 1
    for i in range(1, N + 1):
        cur *= i
        cur %= MOD

    print(cur)


if __name__ == '__main__':
    main()
