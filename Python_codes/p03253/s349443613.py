N,M=map(int,input().split())
import math


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
from collections import Counter
L=prime_factorize(M)
c=Counter(L)
k=[]
for v in c.values():
  k.append(v)
mod=10**9+7
P=[1 for i in range(10**6+1)]
for i in range(10**6):
  P[i+1]=P[i]*(i+1)%mod


def comb(a,b):
  return P[a]*pow(P[a-b],mod-2,mod)*pow(P[b],mod-2,mod)%mod
ans=1
for i in range(len(k)):
  ans*=comb(N+k[i]-1,k[i])
  ans%=mod
print(ans)