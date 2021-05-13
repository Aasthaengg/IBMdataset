from collections import deque
H,W = map(int,input().split())
S = []
Blank = 0
for i in range(H):
  temp = str(input());temp = list(temp)
  Blank += temp.count(".")
  S.append(temp)
#print(S,Blank)
INF = float("inf")
Q = deque([])
Q.append([0,0])
dxdy = [[1,0],[-1,0],[0,1],[0,-1]]
visited = [[INF]*W for _ in range(H)]
visited[0][0] = 1
while Q:
  temp = Q.popleft()
  x = temp[0]; y = temp[1]
  for i in range(4):
    nx = x+dxdy[i][0]
    ny = y+dxdy[i][1]
    if 0<=nx<H and 0<=ny<W and visited[nx][ny] == INF and S[nx][ny] == ".":
      visited[nx][ny] = visited[x][y] + 1
      Q.append([nx,ny])
      if [nx,ny] == [H,W]:
        break
#print(visited)
if visited[H-1][W-1] == INF:
  print(-1)
  exit()
ans = Blank - visited[H-1][W-1]
print(ans)