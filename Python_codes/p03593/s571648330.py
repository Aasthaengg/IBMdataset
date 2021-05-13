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
h,w=map(int,input().split())
a=[input() for _ in range(h)]
cnt={}
for i in range(h):
    ar=a[i]
    for j in ar:
        if j in cnt:
            cnt[j]+=1
        else:
            cnt[j]=1
if h%2==0:
    if w%2==0:
        for i in cnt:
            if cnt[i]%4!=0:
                print("No")
                break
        else:
            print("Yes")
    else:
        res=0
        for i in cnt:
            if cnt[i]%4!=0 and cnt[i]%4!=2:
                print("No")
                break
            elif cnt[i]%4==2:
                res+=1
        else:
            if res>h//2:
              print("No")
            else:
              print("Yes") 
else:
    res=0
    if w%2==0:
        for i in cnt:
            if cnt[i]%4!=0 and cnt[i]%2==0:
                res+=1
            elif cnt[i]%2!=0:
                print("No")
                break
        else:
            if res>w//2:
                print("No")
            else:
                print("Yes")
    else:
        res1=0
        for i in cnt:
            if cnt[i]%4!=0  and cnt[i]%2==1:
                res1+=1
            if cnt[i]%4!=0 and cnt[i]%2==0:
                res+=1       
        if res1==1 and res<=(h-1)//2+(w-1)//2:
            print("Yes")
        else:
            print("No")