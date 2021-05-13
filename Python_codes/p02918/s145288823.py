n,k=map(int,input().split())
from itertools import *
print(min(n-len(list(groupby(input())))+k*2,n-1))