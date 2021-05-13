#幅優先探索
H,W=map(int,input().split())
sy,sx=0,0
gy,gx=H-1,W-1
MAZE=[0]*H
queue=[]
queue.append([sy,sx])
black=0
for i in range(H):
  MAZE[i]=list(str(input()))
  black+=MAZE[i].count('#')
MAZE[sy][sx]='#'

d=[[100000000]*W for i in range(H)]
d[sy][sx]=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
goal=0
while len(queue)>0:
  #Qを取り出す
  Q=queue.pop(0)
  move=d[Q[0]][Q[1]]
  #もし取り出したところがゴールなら出力して終了
  if Q==[gy,gx]:
    goal=1
    break
  #4方向をループする
  for j in range(4):
    y=Q[0]+dy[j]
    x=Q[1]+dx[j]
    if 0<=y<H and 0<=x<W and MAZE[y][x] == '.':
      queue.append([y,x])
      MAZE[y][x] = '#'
      d[y][x] = move+1
if goal==1:
    print(H*W-black-move-1)
else:
    print(-1)