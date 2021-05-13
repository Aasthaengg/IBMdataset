from collections import deque

def bfs(que,d): #幅優先探索
  #いつもはここで定義
  #入力のグラフを初期化
  #d = [[float("inf")] * w for i in range(h)] 
  #que = deque([])
  #que.append((sx,sy))
  #d[sx][sy] = 0
  
  dx = [-1,0,0,1]
  dy = [0,-1,1,0]
  
  while que:
    lead_h,lead_w = que.popleft()
    lead = d[lead_h][lead_w]
    #lead == queの先頭にある要素を取り出す
    for i in range(4):
      nx = lead_w + dx[i]
      ny = lead_h + dy[i]
      if ny<0 or h<=ny or nx<0 or w<=nx:
        #範囲外の場合
        continue
      if d[ny][nx]==float("inf"):
        d[ny][nx] = lead + 1
        que.append((ny,nx))
  return lead

h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]

#多点スタートなのでbfs()内で定義して初期化しない
d = [[float("inf")] * w for i in range(h)] 

#キューも同様
que = deque([])
for i in range(h):
  for j in range(w):
    if maze[i][j] == "#":
      que.append((i,j))
      #各"#"を入れる
      d[i][j] = 0

#print(bfs())
lead = bfs(que,d)
print(lead)