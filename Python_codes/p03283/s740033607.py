import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def count(tsum, l, r):

    return tsum[r][r] - tsum[l - 1][r] - tsum[r][l - 1] + tsum[l - 1][l - 1]


def main():
    N, M, Q = in_nn()
    t = in_na()
    t = list(zip(t, t))
    L = t[:M]
    p = t[M:]

    tsum = np.zeros((N + 1, N + 1), np.int32)
    for i in range(M):
        a, b = L[i]
        a, b = a, b
        tsum[a][b] += 1

    tsum = np.cumsum(tsum, axis=0)
    tsum = np.cumsum(tsum, axis=1)

    for i in range(Q):
        l, r = p[i]
        print(count(tsum, l, r))


if __name__ == '__main__':
    main()
