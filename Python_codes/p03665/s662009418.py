n,p=map(int,input().split())
a=list(map(int,input().split()))
k=0
g=0
for i in range(n):
    if a[i]%2==0:
        g+=1
    else:
        k+=1
from operator import mul
from functools import reduce
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
numg=0
numk=0
if p==0:
    for i in range(k//2+1):
        numk+=cmb(k,i*2)
    for i in range(g+1):
        numg+=cmb(g,i)
    print(numk*numg)
else:
    for i in range((k+1)//2):
        numk+=cmb(k,i*2+1)
    for i in range(g+1):
        numg+=cmb(g,i)
    print(numk*numg)
