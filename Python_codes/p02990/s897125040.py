import math
import collections
import fractions
import itertools
import functools
import operator

def ncr(n, r):
    if n < r: return 0
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = functools.reduce(operator.mul, range(n, n-r, -1), 1)
    denom = functools.reduce(operator.mul, range(1, r+1), 1)
    return numer // denom

def solve():
    n, k = map(int, input().split())
    for i in range(1,k+1):
        ans = (ncr(k-1, i-1) * ncr(n-k+1, i)) % (10**9+7)
        print(int(ans))
    return 0

if __name__ == "__main__":
    solve()
