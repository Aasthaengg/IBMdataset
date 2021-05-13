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
for i in range(n):
    lol.append([a[i],i+1])
lol.sort()
for i in lol:
    print(i[1],end=" ")