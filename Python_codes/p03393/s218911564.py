#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
s=input()
res=[0]*26
n=len(s)
if n!=26:
    for c in s:
        res[ord(c)-ord('a')]=1
    for i in range(26):
        if res[i]==0:
            ans=i
            break
    print(s+chr(ans+ord('a')))
else:
    s=list(s)
    res=[]
    for i in range(n-1):
        if ord(s[n-1-i])-ord(s[n-2-i])>0:
            idx=ord(s[n-2-i])
            res.sort()
            if not res:
              s[n-1-i],s[n-2-i]=s[n-2-i],s[n-1-i]
              print("".join(s[:n-1-i]))
              exit()
            ch=bisect.bisect_right(res,idx)
            if ch==len(res):
                res=[chr(i) for i in res]
                res.append(s[n-2-i])
                ans=[]
                for j in range(n):
                    if j!=n-2-i:
                        ans.append(s[j])
                    else:
                        ans.append(s[n-1-i])
                        break
                print(''.join(ans))
            else:
                minc=chr(res[ch])
                ans=[]
                for j in range(n):
                    if j!=n-2-i:
                        ans.append(s[j])
                    else:
                        ans.append(minc)
                        break
                print(''.join(ans))
            break
        else:
            res.append(ord(s[n-1-i]))
    else:
        print(-1)