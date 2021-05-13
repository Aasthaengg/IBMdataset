x,y = map(int,input().split())
import sys

a = (2*x-y)/3
b = (2*y-x)/3
if not (a.is_integer() and  b.is_integer()) or 2*x<y or 2*y<x:
    print(0)
    sys.exit()
    
a = int(a)
b = int(b)

from functools import reduce
def mycmb(n,r,p):
    r = min(r,n-r)
    if r == 0:
        return 1
    over = reduce(lambda x,y:x*y%p,range(n,n-r,-1))
    under = reduce(lambda x,y:x*y%p,range(1,r+1))
    return (over * pow(under,p-2,p))%p

mod = 10**9+7
print(mycmb(a+b,a,mod))
