from collections import deque
import sys
sys.setrecursionlimit(300000)

N,M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  l,r,d = map(int, input().split())
  l,r = l-1,r-1
  E[l].append((r,d))
  E[r].append((l,-d)) 
  
#for e in E:
#  print(e)
  
# dfs
visited = [False] * N

INF = 10**16
A = [ INF ] * N

def dfs(now, prev, num):
  visited[now] = True
  if A[now] == INF:
    A[now] = num
  else:
    pass
  for nxt, dis in E[now]:
    if nxt == prev:
      continue
    if A[nxt] < INF and A[nxt] != num + dis:
      # ある点において2通りのnum設定の仕方がある
      print("No")
      exit(0)
    if visited[nxt]:
      continue
    dfs(nxt, now, num + dis)
  return 

for i in range(N):
  if visited[i]:
    continue
  dfs(i,-1,0)
  
print("Yes")