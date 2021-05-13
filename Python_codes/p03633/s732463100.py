import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
ans=1
for i in range(n):
    t=int(input())
    ans=(ans*t)//fractions.gcd(ans,t)
print(ans)