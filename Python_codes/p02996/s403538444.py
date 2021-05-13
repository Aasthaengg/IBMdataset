import sys
input=sys.stdin.readline
import math
from collections import defaultdict,deque
from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

#t=1
t=ii()
lol=[] 
ans=0
for _ in range(t):
    a,b=ml()    
    lol.append([b,a])
lol.sort()
f=0
for i in range(t):
    if(lol[i][1]+ans<=lol[i][0]):
        ans+=lol[i][1]
    else:
        f=1
        break
if f:
    print("No")
else:
    print("Yes")