import numpy as np
from math import gcd
n,k=map(int,input().split())
a=list(map(int,input().split()))
if k in a:
    print("POSSIBLE")
    exit()
x=np.gcd.reduce(a)
if x==1:
    print("POSSIBLE")
else:
    if k<max(a) and k%x==0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")