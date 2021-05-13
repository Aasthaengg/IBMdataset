import sys
from collections import Counter
from collections import deque
import math
import fractions
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

s=input()
n=len(s)
c0=0
c1=0
for i in range(n):
    if s[i]=="0":
        c0+=1
    else:
        c1+=1
print(2*min(c0,c1))