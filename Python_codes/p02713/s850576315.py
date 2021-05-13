n=int(input())
from math import gcd
import itertools
lst=[i for i in range(1,n+1)]
kumi=list(itertools.combinations_with_replacement(lst,3))
ans=0
for i in range(len(kumi)):
    a=kumi[i][0]
    b=kumi[i][1]
    c=kumi[i][2]
    g=gcd(gcd(a,b),c)
    if a==b==c:
        ans+=g
    elif a==b or a==c or b==c:
        ans+=3*g
    else:
        ans+=6*g

print(ans)