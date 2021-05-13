from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
#from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.buffer.readline().strip().decode()
def mdata(): return map(int, data().split())
out=sys.stdout.write
#sys.setrecursionlimit(100000)
INF=int(1e9)
mod=int(1e9)+7


n,m=mdata()
matrix = [data() for i in range(n)]
dp=[[0]*m for i in range(n)]
if matrix[0][0]!='#':
    dp[0][0]=1
for i in range(n):
    for j in range(m):
        if matrix[i][j]=='#':
            continue
        if i>0:
            dp[i][j]=(dp[i][j]+dp[i-1][j])%mod
        if j>0:
            dp[i][j]=(dp[i][j]+dp[i][j-1])%mod
print((dp[-1][-1])%mod)



