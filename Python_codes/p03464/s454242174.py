import sys
import math

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    K = int(input())
    A = list(map(int, input().split()))

    # ラウンドiにおける通過者を保存
    m = 2
    M = 2
    for i in range(K - 1, -1, -1):
        n = (m + A[i] - 1) // A[i]
        tmp_m = n * A[i]
        tmp_M = (M // A[i]) * A[i] + A[i] - 1
        if tmp_m > M or tmp_M < m:
            print(-1)
            return
        m = tmp_m
        M = tmp_M

    print(m, M)


if __name__ == "__main__":
    main()
