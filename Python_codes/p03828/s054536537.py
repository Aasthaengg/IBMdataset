from collections import defaultdict
from functools import reduce
from math import sqrt
def factorint(n):
    d = {}
    for i in range(2, int(sqrt(n))+1):
        c = 0
        q, r = divmod(n, i)
        while not r:
            c += 1
            n = q
            q, r = divmod(n, i)
        if c:
            d[i] = c
    if n != 1:
        d[n] = 1
    return d

n = int(input())
mod = 10**9 + 7
A = defaultdict(lambda:1)
for i in range(1, n+1):
    for k, v in factorint(i).items():
        A[k] += v

print(reduce(lambda x, y: x*y % mod, A.values()) if A else 1)