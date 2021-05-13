#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect

n=int(input())
s=[input() for _ in range(n)]
ans=0
bn=an=0
d=0
for i in range(n):
    ans+=s[i].count("AB")
    if s[i][0]=="B":
        an+=1
        if s[i][-1]=="A":
            d+=1
    if s[i][-1]=="A":
        bn+=1
if an==0 or bn==0:
  print(ans)
  exit()
if bn==an==d:
    print(ans+d-1)
else:
    print(ans+min(an,bn))