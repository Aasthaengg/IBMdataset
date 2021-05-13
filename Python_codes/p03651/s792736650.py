from math import gcd
from functools import reduce
n,k=map(int,input().split())
a=list(map(int,input().split()))
m=reduce(gcd,a)
if k%m or k>max(a):flag=1
else:flag=0
print(['POSSIBLE','IMPOSSIBLE'][flag])