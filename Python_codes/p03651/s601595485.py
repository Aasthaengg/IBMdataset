import sys
input = sys.stdin.readline
from fractions import gcd
from functools import reduce


def read():
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, K, A


def solve(N, K, A):
    a = reduce(gcd, A)
    if max(A) < K:
        return "IMPOSSIBLE"
    if a > 1 and K % a != 0:
        return "IMPOSSIBLE"
    return "POSSIBLE"


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
