n,p = map(int,input().split())
a = list(map(int,input().split()))
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

g = 0
k=0
for i in a:
    if i%2:
        k+=1
    else:
        g+=1
if p == 0:
    x = 2**g - 1
    y = 0
    for i in range(2,k+1,2):
        y += cmb(k,i)
    ans = y*x + x + y +1
    print(ans)
else:
    x = 2**g-1
    y = 0
    for i in range(1,k+1,2):
        y += cmb(k,i)
    print(y*x+y)
