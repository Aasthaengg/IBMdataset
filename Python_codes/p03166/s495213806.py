import numpy as np
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n,m = map(int,input().split())
g=[[] for _ in range(n)]
for _ in range(m):
      x,y=map(int,input().split())
      g[x-1].append(y-1)
memo = [0]*n
visited = [False]*n
# dp(i):i=0,1,..,n-1:頂点iを始点とした最長のパスを返す
def dp(v):
      if visited[v]:
            return memo[v]
      else:
            res=0
            for u in g[v]:
                  res=max(res,dp(u)+1)
            memo[v]=res
            visited[v]=True
            return res
for i in range(n):
      dp(i)
print(max(memo))
