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


def check(lol,x):
    if(len(lol)==n):
        tp=0
        for j in v:
            a=j[0]
            b=j[1]
            c=j[2]
            d=j[3]
            if(lol[b-1]-lol[a-1]==c):
                tp+=d
            
        return tp
    k=0         
    for i in range(x,m+1):
        yo=lol[:]
        yo.append(i);
        k=max(k,check(yo,i))
    return k
    


n,m,q=ml()
lol=[]
for i in range(1,m+1):
    lol.append(i)


v=[]

for i in range(q):
   tmp=ll()
   v.append(tmp)



lol=[1]
print(check(lol,1))
