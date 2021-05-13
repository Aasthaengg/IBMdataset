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

n=int(input())
s=input()
mae=[0]*(n+2)
usiro=[0]*(n+2)
for i in range(1,n+1):
    if s[i-1]=="#":
        mae[i]+=1
    mae[i]+=mae[i-1]
    if s[n-i]==".":
        usiro[n-i+1]+=1
    usiro[n-i+1]+=usiro[n-i+2]

ans=2*n
for i in range(1,n+2):
    ans=min(ans,mae[i-1]+usiro[i])
print(ans)
