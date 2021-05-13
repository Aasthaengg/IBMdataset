import math
from collections import defaultdict,deque
from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

n=ii()
a=ll()
a[0]-=1
for i in range(1,n):
    if(a[i]-1>=a[i-1]):
        a[i]-=1
f=0        
for i in range(1,n):
    if(a[i]<a[i-1]):
        f=1
        break
if f:
    print("No")
else:
    print("Yes")