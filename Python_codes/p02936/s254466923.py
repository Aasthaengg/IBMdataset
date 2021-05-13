import sys
sys.setrecursionlimit(10**7)
 
N, Q = map(int, input().split())
root = [[] for i in range(N)]
ans = [0]*N
 
for i in range(N-1):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  root[a].append(b)
  root[b].append(a)

for i in range(Q):
  p, x = map(int, input().split())
  ans[p-1] += x
  
visit = [False]*N
def dfs(n):
  visit[n] = True
  for go in root[n]:
    if visit[go]:
      continue
    ans[go] += ans[n]
    dfs(go)

dfs(0)
print(*ans)