import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M, K = map(int, input().split())
    for n in range(N + 1):
        for m in range(M + 1):
            num = N * m + M * n - 2 * m * n
            if K == num:
                print("Yes")
                return

    print("No")
    return


if __name__ == "__main__":
    main()
