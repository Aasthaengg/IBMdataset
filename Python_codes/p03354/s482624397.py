import sys
sys.setrecursionlimit(10 ** 7)
n, m =map(int, input().split())
pp = list(map(int, input().split()))
p = [i-1 for i in pp]

xy = [[] for i in range(n)]
for i in range(m):
  x, y = map(int, input().split())
  x,y = x-1,y-1
  xy[x].append(y)
  xy[y].append(x)
visited = [0 for i in range(n)]

def dfs(s,cnt):
  visited[s] = cnt
  for i in xy[s]:
    if visited[i] == 0:
      dfs(i,cnt)

cnt = 0
for i in range(n):
  if visited[i]:
    continue
  cnt += 1
  dfs(i,cnt)
ans = 0
for i in range(n):
  if visited[p[i]] == visited[i]:
    ans += 1
print(ans)