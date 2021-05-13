ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
nmax = 2*10**6+2
mod = 10**9+7
fac = [1]*nmax
finv = [1]*nmax
inv = [1]*nmax
def ncr_pre():
    for i in range(2,nmax):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod%i] * (mod//i) %mod
        finv[i] = finv[i-1] * inv[i] %mod

def ncr(n,r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fac[n]* (finv[r] * finv[n-r] %mod) %mod

ncr_pre()
k = ni()
s = input()
n = len(s)
ans= 0
for i in range(k+1):
    ans=(ans+ ncr(n+k-i-1,n-1)*pow(25,k-i,mod)*pow(26,i,mod) )%mod
print(ans)
