from math import gcd
from functools import reduce

m,k = map(int,input().split())
L = list(map(int,input().split()))

v = reduce(gcd,L)
maxL = max(L)

if k > maxL:
    print("IMPOSSIBLE")
    exit()
if k in L:
    print("POSSIBLE")
    exit()
    
if (maxL - k)%v == 0:
    print("POSSIBLE")
    exit()
print("IMPOSSIBLE")