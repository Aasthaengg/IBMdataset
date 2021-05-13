import sys
import numpy as np

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M, Q = map(int, input().split())
    lines = np.zeros((N + 1, N + 1)).astype(np.int32)

    for _ in range(M):
        l, r = map(int, input().split())
        lines[l, r] += 1

    lines = np.cumsum(lines, axis=0)
    lines = np.cumsum(lines, axis=1)

    for _ in range(Q):
        p, q = map(int, input().split())
        # 終点がq以下のものの総数から，始点がp-1以下で終点がq以下のものをひく
        print(lines[-1][q] - lines[p - 1][q])


if __name__ == "__main__":
    main()
