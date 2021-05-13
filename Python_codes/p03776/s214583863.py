from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


n,a,b=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()

print(sum(lst[-a:])/a)

pin=lst[-a]
ans=0

l=lst[:-a].count(pin)
r=lst[-a:].count(pin)


if pin*a==sum(lst[-a:]):
    cnt=0
    for i in range(a,min(b,l+r)+1):
        cnt+=cmb(l+r,i)
    
    print(cnt)
    exit()


print(cmb(l+r,r))
