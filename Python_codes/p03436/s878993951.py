from collections import deque

h,w = list(map(int,input().split()))
black_num = 0
graph = []
for _ in range(h):
  tmp=input()
  black_num+=tmp.count("#")
  graph.append(list(tmp))
#graph=[list(input()) for _ in range(h)]#graph初期化

sx = 0
sy = 0
gx = h-1
gy = w-1

dist=[[-1 for j in range(w)] for i in range(h)]#distance設定
dist[sx][sy]=0#スタート地点は初期値0
 
que = deque([(sx,sy,0)])#スタート地点とdist初期値を入力
 
while que:
  u,v,z = que.popleft()
  for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
    if not (0<=u+i<h and 0<=v+j<w):#座標がh,w内でなければ探索しない
      continue
    elif graph[u+i][v+j]=="#":#壁なら探索しない
      continue
    elif dist[u+i][v+j]>0:#すでに訪れていたら探索しない
      continue

    dist[u+i][v+j]=z+1#距離を前回の＋1
    que.append([u+i,v+j,z+1])#訪れてないのでqueに今の地点を追加する

if dist[gx][gy]==-1: #ゴールまでたどり着けない場合
  print(-1)
else:
  print(h*w-(dist[gx][gy]+1)-black_num)