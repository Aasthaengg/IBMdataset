import numpy as np
from functools import reduce
from operator import add,sub,mul,truediv
from fractions import gcd


n = int(input())

a = list(map(int,input().split()))

a = np.array(a)

a = np.insert(a,0,0)
a = np.append(a,0)

org = 0
dis = []
for i in range(1,n+2):
    org += abs(a[i]-a[i-1])
    dis.append(abs(a[i]-a[i-1]))

#print(org)
#print(dis)


for i in range(1,n+1):
    print(org - dis[i-1]-dis[i]+abs(a[i+1]- a[i-1]))
