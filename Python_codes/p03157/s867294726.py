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
h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
seen={}
check=[[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            seen[i*w+j]=0
if not seen:
    print(0)
    exit()
d=deque()
p=[[1,0],[-1,0],[0,1],[0,-1]]
ans=0

for j in seen:
    if seen[j]==0:
        d.append(j)
        blue=1
        white=0
        seen[j]=1    
        while d:
            i=d.pop()
            if i==0:
                f=True if s[0][0]=="#" else False
            else:
                f=True if i>0 else False
            ih=abs(i)//w
            iw=abs(i)%w
            check[ih][iw]=1
            for v in p:
                x,y=v
                if f==True and 0<=x+iw<w and 0<=y+ih<h and s[y+ih][x+iw]=="." and check[y+ih][x+iw]==0:
                    d.append(((ih+y)*w+(iw+x))*(-1))
                    white+=1
                    check[y+ih][x+iw]=1
                elif f==False and 0<=x+iw<w and 0<=y+ih<h and s[y+ih][x+iw]=="#" and check[y+ih][x+iw]==0:
                    d.append(((ih+y)*w+(iw+x)))
                    seen[((ih+y)*w+(iw+x))]=1
                    check[y+ih][x+iw]=1
                    blue+=1
        ans+=blue*white
print(ans)