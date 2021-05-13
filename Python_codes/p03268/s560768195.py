import sys
input = sys.stdin.readline
import math


def read():
    N, K = map(int, input().strip().split())
    return N, K


def solve(N, K):
    # Kの倍数の数
    nk = math.floor(N / K)
    if K % 2 == 1:
        return nk ** 3
    else:
        nhk = math.floor(N / (K//2))
        return nk ** 3 + (nhk - nk) ** 3


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
