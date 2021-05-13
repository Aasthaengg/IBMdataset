from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
#from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.buffer.readline().strip().decode()
def mdata(): return map(float, data().split())
out=sys.stdout.write
#sys.setrecursionlimit(100000)
INF=int(1e9)
mod=int(1e9)+7


n=int(data())
P=list(mdata())
dp=[0]*(n//2+2)
dp[1]=1
for i in range(n):
    dp1=dp[:]
    for j in range(1,len(dp)):
        k=dp[j-1]*(1-P[i])+dp[j]*(P[i])
        dp1[j]=k
    dp=dp1[:]
print(sum(dp))


