import numpy as np
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N,M=map(int,list(input().split(" ")))
mod=10**9+7
def factor(n):
    fct = []  
    b, e = 2, 0 
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

fac=np.array(factor(M))
ans=1
for i in range(len(fac)):
    ans*=cmb(N+fac[i][1]-1,N-1)
print(ans%mod)