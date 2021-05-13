from operator import mul
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n-r, -1), 1)
    under = reduce(mul, range(1, r+1), 1)
    return over // under

A = input()
strs = set(list(A))

ans = len(A) * (len(A)-1) // 2
for s in strs:
    num = A.count(s)

    if num >= 2:
        ans -= nCr(num, 2)

print(ans+1)