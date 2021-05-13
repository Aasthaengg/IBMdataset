import sys


sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())

    if N % 2 == 0:
        for i in range(M):
            x = i + 1
            y = N - i - 1
            if y - x > (N - y + x):
                print(x, y)
            else:
                print(x, y - 1)
    else:
        for i in range(M):
            print(i + 1, N - i)


if __name__ == "__main__":
    main()
