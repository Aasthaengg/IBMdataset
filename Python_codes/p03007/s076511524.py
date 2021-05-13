from collections import *
from heapq import *
from itertools import *
from fractions import gcd
import sys
from decimal import *
import copy
from bisect import *
input=lambda :sys.stdin.readline().rstrip()
N=int(input())
A=list(map(int,input().split()))
if N==2:
    A.sort()
    print(A[1]-A[0])
    print(A[1],A[0])
else:
    plus= [i for i in A if i>=0]
    minus=[i for i in A if i<0]

    plus.sort(reverse=True)
    minus.sort()
    lst=[]
    if not minus:
        a=plus.pop()
        b=plus.pop()
        minus.append(a-b)
        lst.append([a,b])
    if not plus:
        a=minus.pop()
        b=minus.pop()
        plus.append(a-b)
        lst.append([a,b])

    while len(plus)>1:
        a=plus.pop()
        lst.append([minus[0],a])
        minus[0]-=a

    while len(minus)>1:
        a=minus.pop()
        lst.append([plus[0],a])
        plus[0]-=a

    print(plus[0]-minus[0])
    lst.append([plus[0],minus[0]])
    for a,b in lst:
        print(a,b)
