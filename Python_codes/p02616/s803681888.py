#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
z=-1
p=-1
mod=10**9+7
ans=1
for i in range(n):
    if a[i]==0:
        z=i
    elif a[i]>0:
        p=i
        break
a_abs=sorted(a,key=abs,reverse=True)
if (p==-1 and k%2==1) or n==k:
    for i in range(k):
        ans*=a[n-1-i]
        ans%=mod
    print(ans%mod)
    exit()
else:
    lp=-1
    lm=-1
    f=0
    for i in range(k):
        if a_abs[i]>=0:
            lp=i
        else:
            lm=i
            f+=1
    if f%2==0:
        for i in range(k):
          ans*=a_abs[i]
          ans%=mod
        print(ans)
    else:
        fp=-1
        fm=-1
        check_p=False
        check_m=False
        for i in range(k,n):
            if not check_p and a_abs[i]>=0:
                fp=i
                check_p=True
            elif not check_m and a_abs[i]<0:
                fm=i
                check_m=True
            if check_m and check_p:
                break
        if lp!=-1:
            if fp==-1:
              for i in range(k):
                if i==lp:
                  continue
                ans*=a_abs[i]
                ans%=mod
              ans*=a_abs[fm]
              ans%=mod
            elif fm==-1:
              for i in range(k):
                if i==lm:
                  continue
                ans*=a_abs[i]
                ans%=mod
              ans*=a_abs[fp]
              ans%=mod

            else:
                if a_abs[fm]*a_abs[lm]>=a_abs[fp]*a_abs[lp]:
                  for i in range(k):
                    if i==lp:
                      continue
                    ans*=a_abs[i]
                    ans%=mod
                  ans*=a_abs[fm]
                  ans%=mod
                else:
                  for i in range(k):
                    if i==lm:
                      continue
               	    ans*=a_abs[i]
                    ans%=mod
                  ans*=a_abs[fp]
                  ans%=mod
        else:
          for i in range(k):
            if i==lm:
              continue
            ans*=a_abs[i]
            ans%=mod
          ans*=a_abs[fp]
          ans%=mod
        print(ans%mod)