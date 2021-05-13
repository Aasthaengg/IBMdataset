import sys
import math
from collections import defaultdict,deque
from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()
sys.setrecursionlimit(10**6)
"""========main code==============="""

t=1
for _ in range(t):
    a,b,c=ml()
    d=(c+1)//b
    d*=b
    if(d!=0):
        d-=1
    else: d=c    
    print((a*d)//b-a*(d//b))