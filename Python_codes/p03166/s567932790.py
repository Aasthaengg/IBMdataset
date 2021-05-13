# import sys
import sys,os,io
# input = sys.stdin.readline
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
  a,b = map(int, input().split())
  edge[a-1].append(b-1)

def dfs(start):
  stack = [start]
  while stack:
    v = stack[-1]
    marker = 0
    path_l[v] = 0
    for u in edge[v]:
      if path_l[u]==-1: #子へ降ろす
        marker = 1
        stack.append(u)
      else: #子から吸い上げる
        #吸い上げる際の個々の処理
        path_l[v] = max(path_l[v], path_l[u]+1)
    if marker==0:
      stack.pop()
  return

path_l = [-1]*N
for i in range(N):
  if path_l[i]==-1:
    dfs(i)
ans = max(path_l)
print(ans)
