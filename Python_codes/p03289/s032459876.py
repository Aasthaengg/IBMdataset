#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect
s=input()
c=False
if s[0]=="A":
    for i in range(1,len(s)):
        if s[i]!="C" and s[i].isupper():
            print("WA")
            break
        elif s[i]=="C" :
            if c==False and 2<=i<=len(s)-2:
                c=True

            else:
                print("WA")
                break
    else:
      if  c:
        print("AC")
      else:
        print("WA")
else:
  print("WA")