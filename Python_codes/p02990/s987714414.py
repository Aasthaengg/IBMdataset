from operator import mul
from functools import reduce
n,k = map(int,input().split())
ans = 0
mod = 10**9+7
def cmb(n, r):
    if r > n:
        return 0
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under
for i in range(1,k+1):
    cnt = cmb(n-k+1,i)* cmb(k-1, i-1)
    print(cnt%mod)