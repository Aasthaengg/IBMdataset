from collections import defaultdict,deque
from sys import stdin,setrecursionlimit
import heapq,bisect,math,itertools,string,queue,datetime,copy
setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, stdin.readline().split()))


H,N = inpl()
AB  = []
for _ in range(N):
    a= inpl()
    AB.append(a)
dp = [[INF]*(H+1) for _ in range(N)]
dp[0][0] = 0
for i in range(N):
    for j in range(H+1):
        at = AB[i][0]
        cost = AB[i][1]
        dp[i][j] = min(dp[i][max(j-at,0)]+cost,dp[max(0,i-1)][j])

print(dp[N-1][H])
