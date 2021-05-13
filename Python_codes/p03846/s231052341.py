import sys
from io import StringIO
import unittest

def resolve():
    readline=sys.stdin.readline
    n=int(readline())
    ai=list(map(int, readline().split()))

    x=[0]*(10**5+1)
    for a in ai:
        x[a]+=1
    
    k=n-1
    x2=0
    while k>=0:
        if k==0 and x[k]==1:
            x2+=0
        elif x[k]==2:
            x2+=1
        else:
            print(0)
            return
        k-=2
    
    print(pow(2,x2,10**9+7))
resolve()