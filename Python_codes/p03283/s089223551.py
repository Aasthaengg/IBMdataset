import sys
import numpy as np

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, M, Q = map(int, readline().split())
    LR = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        L, R = map(int, readline().split())
        LR[L][R] += 1

    LR = np.array(LR)
    LR = LR.cumsum(axis=0).cumsum(axis=1)

    for _ in range(Q):
        p, q = map(int, readline().split())
        ans = LR[q][q] - LR[q][p - 1] - LR[p - 1][q] + LR[p - 1][p - 1]
        print(ans)


if __name__ == '__main__':
    main()
