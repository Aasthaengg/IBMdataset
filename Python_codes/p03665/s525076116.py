import sys
from scipy.special import comb
import functools
import operator

"""def sum(l):
    result = functools.reduce(operator.mul, l)
    return result"""

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

N, P = nm()
A = nl()
even = 0
odd = 0
for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
if P == 0:
    ans = sum([comb(even, i, exact=True) for i in range(0, even+1)]) * sum([comb(odd, i, exact=True) for i in range(0, odd+1, 2)])
else:
    ans = sum([comb(even, i, exact=True) for i in range(0, even+1)]) * sum([comb(odd, i, exact=True) for i in range(1, odd+1, 2)])
print(ans)