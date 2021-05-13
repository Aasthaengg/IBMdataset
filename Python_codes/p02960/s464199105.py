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


mod=10**9+7
s=input()
n=len(s)
dp=[[0]*13 for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(13):
        if s[i]=="?":
            for k in range(10):
                dp[i+1][(j*10+k)%13]+=dp[i][j]
                dp[i+1][(j*10+k)%13]%=mod
        else:
            dp[i+1][(j*10+int(s[i]))%13]+=dp[i][j]
            dp[i+1][(j*10+int(s[i]))%13]%=mod
print(dp[n][5]%mod)