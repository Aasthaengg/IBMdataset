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

n=ii1()
dp=[0]*(n+1)
arr=iia()
a=list(zip(arr,range(1,n+1)))
a.sort()
for i in range(n):
    print(a[i][1],end=' ')
print()

