from collections import Counter
from collections import deque
import math
import bisect
import sys
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

mod=1000000007
n,m=sorted(mp())
if m-n>1:
    ans=0
elif m-n==1:
    ans=m
    for i in range(1,n+1):
        ans*=i**2
        ans%=mod
else:
    ans=2
    for i in range(1,n+1):
        ans*=(i**2)
        ans%=mod
print(ans%mod)
