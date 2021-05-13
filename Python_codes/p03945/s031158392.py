import sys
from collections import Counter
from collections import deque
import math
import bisect
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

s=input()
n=len(s)
ans=0
for i in range(n-1):
    if s[i]!=s[i+1]:
        ans+=1
print(ans)