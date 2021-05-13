import math
from collections import defaultdict,deque
#from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

n=ii()
a=ll()
lol=[]
lol.append(a[0])
for i in range(1,n-1):
    lol.append(min(a[i-1],a[i]))
lol.append(a[n-2])
print(sum(lol))