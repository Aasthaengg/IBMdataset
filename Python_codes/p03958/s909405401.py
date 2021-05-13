n,t,*a=map(int,open(0).read().split())
from math import *
print(max(0,(max(a)-ceil(n/2))*2-1))