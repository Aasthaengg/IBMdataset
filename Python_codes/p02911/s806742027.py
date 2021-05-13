import math
from collections import defaultdict,deque
#from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

a,b,c=ml()
lol=[b]*a
for i in range(c):
    n=ii()
    lol[n-1]+=1
    
for i in lol:
    if(i-c>0): print("Yes")
    else: print("No")    
