from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
#from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.buffer.readline().strip().decode()
def mdata(): return map(int, data().split())
out=sys.stdout.write
#sys.setrecursionlimit(100000)
INF=int(10e9)


n,m=mdata()
dp=[0]*n
g=[set() for i in range(n)]
par=[i for i in range(n)]
chl=[0]*n
for i in range(m):
    x,y=mdata()
    g[x-1].add(y-1)
    chl[y-1]=1
vis=[0]*n
for i in range(n):
    if chl[i]==0:
        s1=deque()
        s1.append(i)
        while s1:
            a=s1[-1]
            if vis[a]==1:
                if a!=i:
                    dp[par[a]]=max(dp[par[a]],dp[a]+1)
                s1.pop()
                continue
            vis[a]=1
            for j in g[a]:
                if vis[j]==0:
                    s1.append(j)
                    par[j]=a
                else:
                    dp[a]=max(dp[a],dp[j]+1)
print(max(dp))



