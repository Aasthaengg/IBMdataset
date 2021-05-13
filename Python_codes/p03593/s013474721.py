from collections import *
from heapq import *
from itertools import *
from fractions import gcd
import sys
from decimal import *
import copy
input=lambda :sys.stdin.readline().rstrip()

H,W=map(int,input().split())
S=""
for i in range(H):
    S+=input()
S=Counter(S)
c=0
b=0
a=0

for i in S:

    z=S[i]
    c+=z-z%4
    z%=4
    b+=z-z%2
    z%=2
    a+=z
C=(H-H%2)*(W-W%2)
c-=C
if c<0:
    print("No")
    exit()
b+=c
b-=(H*W//2*2-C)
if b!=0:
    print("No")
    exit()
if a-H*W%2!=0:
    print("No")
    exit()

print("Yes")
