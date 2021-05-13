import sys
from math import floor,ceil
K=int(input())
A=[int(i) for i in input().split()]
def f(x):
    t=x
    for a in A:
        t=t-(t%a)
    return t

mi=0
ma=10**16
while ma-mi>1:
    mid=(ma+mi)//2
    if f(mid)>=2:
        ma=mid
    else:
        mi=mid
left=ma
mi=0
ma=10**16
while ma-mi>1:
    mid=(ma+mi)//2
    if f(mid)<=2:
        mi=mid
    else:
        ma=mid
if left>mi:
    print(-1)
else:
    print(left,mi)