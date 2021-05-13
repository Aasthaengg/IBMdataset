import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

H,W = map(int,input().split())
INF = 10**18
q = []

visited = [[True]*(W+2)]
visited += [[True] + [x == '#' for x in input().rstrip()] + [True] for _ in range(H)]
visited.append([True]*(W+2))
for i in range(1,H+1):
  for j in range(1,W+1):
    if visited[i][j]:
      q.append((i,j))

ans = -1
while q:
  qq = []
  ans += 1
  for x,y in q:
    if not visited[x-1][y]:
      visited[x-1][y] = True
      qq.append((x-1,y))
    if not visited[x+1][y]:
      visited[x+1][y] = True
      qq.append((x+1,y))
    if not visited[x][y-1]:
      visited[x][y-1] = True
      qq.append((x,y-1))
    if not visited[x][y+1]:
      visited[x][y+1] = True
      qq.append((x,y+1))
  q = qq
  
print(ans)