import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right


def read():
    N = int(input().strip())
    A = [int(input().strip()) for _ in range(N)]
    return N, A


def solve(N, A, INF=10**9+1):
    # LIS
    # dp[i]: 長さiの最長増加部分列(A[i]<A[j])のうち、最も小さい数字
    dp = [INF for i in range(N)]
    for i in range(N):
        a = A[N-i-1]
        idx = bisect_right(dp, a)
        dp[idx] = a
    return bisect_right(dp, INF-1)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
