import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M, D = map(int, input().split())

    if D == 0:
        ans = 1 / N
        # 一つの数列中の間隔の数をかける
        ans *= M - 1
    else:
        # 絶対値の差がDになる二つの文字列の並びの数
        cnt = 2 * (N - D)

        # N**2通りの文字の美しさの平均
        ans = cnt / (N ** 2)

        # 一つの数列中の間隔の数をかける
        ans *= M - 1

    print(ans)


if __name__ == "__main__":
    main()
