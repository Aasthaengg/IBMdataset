import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
p = [list(map(int,input().split())) for _ in range(M)]
dp = [-1]*N
ip = [[] for _ in range(N)]
for i in range(M):
  ip[p[i][1]-1].append(p[i][0]-1)

#閉路がないため同じ頂点は通らない
#i番目の頂点に到達するまでの最長手数をメモ化再帰で求める

def maxpath(i):
  if dp[i] != -1:
    return dp[i]
  a = 0
  for el in ip[i]:
    a = max(a,maxpath(el)+1)
  dp[i] = a
  return a
  
for i in range(N):
  maxpath(i)

print(max(dp))