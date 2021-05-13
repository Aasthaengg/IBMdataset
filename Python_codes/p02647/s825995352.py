import sys
from itertools import accumulate
from numba import njit

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

@njit
def solve(n, k, a):
    b = [0]*n
    for _ in range(k):
        for i in range(n):
            if i > a[i]:
                b[i-a[i]] += 1
            else:
                b[0] += 1
            if i + a[i] + 1 < n:
                b[i + a[i] + 1] -= 1
        for i in range(n-1):
            b[i+1] += b[i]
            a[i] = 0
        a[-1] = 0
        b, a = a, b
        if min(a) >= n:
            break
    return a

n, k = nm()
a = nl()
print(*solve(n, k, a))
