import sys
input = sys.stdin.readline
from collections import defaultdict


def read():
    A, B, K = list(map(int, input().strip().split()))
    return A, B, K


def solve(A, B, K):
    d = defaultdict(bool)
    for a in range(A, min(A+K, B+1)):
        d[a] = True
    for b in range(B, max(A-1, B-K), -1):
        d[b] = True
    ans = list(sorted(d.keys()))
    for a in ans:
        print(a)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
