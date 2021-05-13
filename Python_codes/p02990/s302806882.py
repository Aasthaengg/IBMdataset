from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


n,k=map(int,input().split())
mod=10**9+7

red=n-k
sep=red+1


for i in range(1,1+k):
    if i>sep:
        print(0)
        continue
    blue=k-i
    ans=cmb(i+blue-1,blue)*cmb(sep,i)%mod
    print(ans)
