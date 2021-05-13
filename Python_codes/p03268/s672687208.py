N,K=map(int, input().split())
#1~NのKで割ったあまり
ks=0
k2s=0
for i in range(1,N+1):
    if K%2==0:
        if i%K==0:
            ks+=1
        elif i%(K//2)==0:
            k2s+=1
    else:
        if i%K==0:
            ks+=1
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


ans=0
if ks>=1:
    ans+=cmb(ks,1)
if ks>=2:
    ans+=cmb(ks,2)*6
if ks>=3:
    ans+=cmb(ks,3)*6
#print(ks,k2s)
if k2s>=1:
    ans+=cmb(k2s,1)
if k2s>=2:
    ans+=cmb(k2s,2)*6
if k2s>=3:
    ans+=cmb(k2s,3)*6
print(ans)