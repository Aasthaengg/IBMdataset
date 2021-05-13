#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
n,m=map(int,input().split())
a=list(map(int,input().split()))

s=[0]*n
a.sort()
s[0]=a[0]
for i in range(1,n):
    s[i]=s[i-1]+a[i]
res=0
l=0
r=2*a[-1]+1
while r>l+1:
    x=(l+r)//2
    res=0
    for ai in a:
        j=x-ai
        cnt=bisect.bisect_left(a,j)
        res+=(n-cnt)
    if res<m:
        r=x
    else:
        l=x
ans=0
c=0
for ai in a:
    cnt=bisect.bisect_left(a,l-ai)
    ans=ans+ai*(n-cnt)+(s[-1]-s[cnt-1]) if cnt!=0 else ans+ai*(n-cnt)+s[-1]
    c+=(n-cnt)
ans-=(c-m)*l
print(ans)
