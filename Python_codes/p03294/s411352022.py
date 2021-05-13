import sys
import numpy as np
import math
from functools import reduce
sys.setrecursionlimit(10**6)

n=int(input())
a=list(map(int,input().split()))

b=1
for i in range(n):
    b*=a[i]

#def lcm_base(x,y):
#    return (x*y)//math.gcd(x,y)
#def lcm_list(numbers):
#    return reduce(lcm_base, numbers, 1)
#c=lcm_list(a)

#print(b)
#print(c)

ans=0
for j in range(n):
    ans+=(b-1)%a[j]
#    ans+=(c-1)%a[j]

#ans=0
##for i in range(b):
#for i in range(c):
#    f=0
#    for j in range(n):
#        f+=(i+1)%a[j]
#    ans=max(ans,f)

print(ans)

