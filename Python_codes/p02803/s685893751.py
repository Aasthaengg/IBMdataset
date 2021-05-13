from collections import deque
import numpy as np

h,w=list(map(int,input().split()))
graph=[input() for _ in range(h)]#graph初期化

def f(x,y):#start地点(x,y)
  x-=1;y-=1
  dist=[[-1 for j in range(w)] for i in range(h)]#distance設定
  dist[x][y]=0#スタート地点は初期値0
  que = deque([(x,y,0)])#スタート地点とdist初期値を入力 

  while que:#queの中身がある限り
    r,s,t = que.popleft()
    for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:#これでi,jとれるの
      if not (0<=r+i<h and 0<=s+j<w):#座標がh,w内でなければ探索しない
        continue
      if dist[r+i][s+j]>=0:#すでに訪れていたら探索しない。>=
        continue
      if graph[r+i][s+j]=="#":#壁なら探索しない
        continue
      dist[r+i][s+j]=t+1#距離を前回の＋1
      que.append([r+i,s+j,t+1])#訪れてないのでqueに今の地点を追加する
  return np.amax(dist)#2次元配列の最大値を返す
ans=0
for i in range(1,h+1):#全探索（indexのため1~h+1まで）
  for j in range(1,w+1):
    if graph[i-1][j-1]=="#":#壁なら探索しない
      continue
    ans=max(ans,f(i,j))
print(ans)