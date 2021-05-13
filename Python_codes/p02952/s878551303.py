import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

ans=0
for i in range(1,int(input())+1):
    if len(str(i))%2==1:
        ans+=1
print(ans)