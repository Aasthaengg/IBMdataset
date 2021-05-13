import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    A, B, C = map(int, input().split())

    ans1 = abs(A // 2 * B * C - (A - A // 2) * B * C)
    ans2 = abs(B // 2 * A * C - (B - B // 2) * A * C)
    ans3 = abs(C // 2 * B * A - (C - C // 2) * B * A)
    print(min(ans1, ans2, ans3))


if __name__ == "__main__":
    main()
