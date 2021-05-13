import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations
from itertools import accumulate
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=10**9+7

s=input()
# lst=[0,0]
ans=0
for i in range(len(s)):
    if i%2==0:
        if s[i]=="g":
            continue
        else:
            ans-=1
    else:
        if s[i]=="g":
            ans+=1
        else:
            continue
print(ans)