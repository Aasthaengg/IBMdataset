import sys

sys.setrecursionlimit(2 * 10 ** 5)

N = int(input())

A = [int(x) for x in input().split()]
A = sorted((a, i) for i, a in enumerate(A))

cache = [[None for i in range(N + 1)] for j in range(N + 1)]


def dp(l, r):
    if l > r:
        return 0
    if cache[l][r] is None:
        a, x = A[r - l]
        cache[l][r] = max(a * abs(x - l) + dp(l + 1, r), a * abs(x - r) + dp(l, r - 1))
    return cache[l][r]


print(dp(0, N - 1))
