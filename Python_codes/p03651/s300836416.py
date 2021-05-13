from math import gcd
from functools import reduce
n,k=map(int,input().split())
a=list((map(int,input().split())))
b=reduce(gcd,a)
print(['IMPOSSIBLE','POSSIBLE'][k%b==0 and k<=max(a)])