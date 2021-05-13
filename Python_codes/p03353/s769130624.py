#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
s=input()
k=int(input())
n=len(s)
a=[chr(i) for i in range(ord('a'),ord('z')+1)]
ans=set()
for i in a:
    if i not in s:
        continue
    if len(ans)>=5:
        break
    for c in range(n):
      if s[c]==i:
          l=c
          r=c
          while True:
            if  r>n or r-l>6:
                break
            ans.add(s[l:r+1])
            r+=1
ans=list(ans)
ans.sort()
print(ans[k-1])
