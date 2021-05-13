from collections import *
from heapq import *
from itertools import *
from fractions import gcd
import sys
from decimal import *
input=lambda :sys.stdin.readline().rstrip()

N=int(input())
if N==1:
    print(1)
    exit()
XY=[list(map(int,input().split())) for i in range(N)]
itelst=combinations(range(N),2)

alst=[]
for a,b in itelst:
    x1,y1=XY[a]
    x2,y2=XY[b]
    Y=y1-y2;X=x1-x2
    if X and Y:
        alst.append([X,Y])
    elif Y or X:
        alst.append([X,Y])



value=50
idlemax=10**18
for Xa,Ya in alst:
    n=set([x+idlemax*y for x,y in XY])

    count=0
    for x,y in XY:
        if x+idlemax*y in n:
            count+=1
            a=0;b=0
            A=x+Xa+a+idlemax*(y+Ya+b)
            while A in n:
                n.remove(A)
                a+=Xa;b+=Ya
                A=x+Xa+a+idlemax*(y+Ya+b)

            a=0;b=0
            A=x-Xa-a+idlemax*(y-Ya-b)
            while A in n:
                n.remove(A)
                a+=Xa;b+=Ya
                A=x-Xa-a+idlemax*(y-Ya-b)
    value=min(value,count)
print(value)
