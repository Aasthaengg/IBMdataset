import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def solve(N, A):
    A.sort()
    n = N-1
    p = bisect_left(A, A[n] / 2)
    low = max(0, p - 1)
    high = min(N - 1, p)
    if n == high:
        return "%d %d" % (A[n], A[low])
    elif A[low] > A[n] - A[high]:
        return "%d %d" % (A[n], A[low])
    else:
        return "%d %d" % (A[n], A[high])


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
