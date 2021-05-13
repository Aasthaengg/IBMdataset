n,m=map(int,input().split())
a=map(int,input().split())

from fractions import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
l=1

max2=0
min2=1000

for i in a:
    factor=(i^(i-1)).bit_length()
    max2=max(max2,factor)
    min2=min(min2,factor)
    l=l*i//2//gcd(l,i//2)
    if l>m:
        break

if l>m or min2!=max2:
    print(0)
else:
    ans=1 if l<=m else 0
    m-=l
    print(ans+max(0,m//(2*l)))