import sys,os
import math
from fractions import Fraction 
from collections import defaultdict
from random import randint

# sys.stderr=open('err.txt','w')
# sys.stdout=open('output.txt','w')
# sys.stdin=open('input.txt','r')

def linput():
    return list(minput())

def minput():
    return map(int, sys.stdin.readline().strip().split())

###############################################################

def make_set(a):
    parent[a]=a
    sizen[a]=1

def find_set(a):
    if parent[a]==a:
        return a
    parent[a]=find_set(parent[a])
    return parent[a]

def union_set(a,b):
    x=find_set(a)
    y=find_set(b)
    if x==y:
        return
    else:
        if sizen[x]>sizen[y]:
            parent[y]=x
            sizen[x]+=sizen[y]
        else:
            parent[x]=y
            sizen[y]+=sizen[x]

n,m=minput()
parent=[0]*n
sizen=[0]*n
for i in range(n):
    make_set(i)
ans=0
for i in range(m):
    x,y=minput()
    if x>y:
        x,y=y,x
    x=x-1
    y=y-1
    union_set(x,y)
# print(parent)
di = defaultdict(int)
# for i in parent:
#     di[i]+=1
# print(di)

for v in sizen:
    ans=max(ans,v)
print(ans)
