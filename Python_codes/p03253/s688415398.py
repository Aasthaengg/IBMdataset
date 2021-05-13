import collections as col
import numpy as np
import math as ma
import scipy.misc as spm #miscellaneous

MOD = 10**9 + 7
def inv(a): return pow(a, MOD-2, MOD)
def comb(n,r):
    ans = ma.factorial(n)%MOD * inv(ma.factorial(r)) * inv(ma.factorial(n-r))
    return ans%MOD

def prime(n):
    ans = []
    for i in range(2, int(n**0.5)+1):
        while not n%i: n //= i; ans.append(i)
    if n != 1: ans.append(n)
    return ans

n,m = map(int,input().split())
cnt = col.Counter(prime(m))

ans = 1
for key,val in cnt.items():
    #ans *= comb(val + n-1, n-1)
    ans *= spm.comb(val + n-1, n-1, exact=1)
    ans %= MOD
print(ans)
