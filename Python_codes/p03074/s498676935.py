import sys
import time
#from collections import deque, Counter, defaultdict
#from fractions import gcd
#import bisect
#import heapq
import math
start=time.time()
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
n,k = rl()

s=rs()
now="1"
cnt=0

nums=[]
for i in s:
    if i==now:
        cnt+=1
    else:
        now=str(1-int(now))
        nums.append(cnt)
        cnt=1
if cnt!=0: nums.append(cnt)

if len(nums)%2==0:nums.append(0)
SUM=[0]
for i in range(len(nums)):
    SUM.append(SUM[i]+nums[i])

skip=2*k+1
ans=0
for i in range(0,len(SUM),2):
    right=min(i+skip, len(SUM)-1)
    left =i
    ans=max(ans,-SUM[left]+SUM[right])
print(ans)