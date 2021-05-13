# Coding is about expressing your feeling, and
# there is always a better way to express your feeling_feelme
import sys
import math
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output2.txt','w')
from sys import stdin,stdout
from collections import deque,defaultdict
from math import ceil,floor,inf,sqrt,factorial,gcd,log2
from copy import deepcopy
ii1=lambda:int(stdin.readline().strip())
is1=lambda:stdin.readline().strip()
iia=lambda:list(map(int,stdin.readline().strip().split()))
isa=lambda:stdin.readline().strip().split()
mod=int(1e9 + 7)

def divisor(n):
    ans={}
    m=int(n**0.5)+1
    for i in range(1,m):
        if n%i==0:
            ans[i]=1
            ans[n//i]=1
    return ans
def prime(n):
    if n<=3:
        return True
    m=int(n**0.5)+1
    if n%2==0:
        return False
    for i in range(3,m,2):
        if n%i==0:
            return False
    return True

a,b=iia()
ans=divisor(a)
ans2=divisor(b)
res=[]
for i,j in ans.items():
    if i in ans2:
        res.append(i)

#print(res)
count=0
for i in res:
    if prime(i):
        count+=1
print(count)

