import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
li2 = [0,0]
li4 = [0]
for key,value in c.items():
    if value>=4:
        li4.append(key)
    elif value>=2:
        li2.append(key)
li2.sort()
li4.sort()
ans1 = li2[-1]*li2[-2]
ans2 = li4[-1]**2
ans3 = li4[-1]*li2[-1]
ans = max(ans1,ans2)
ans = max(ans,ans3)
print(ans)

