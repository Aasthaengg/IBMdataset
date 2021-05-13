from collections import deque

H,W = map(int,input().split())

by,bx= deque(),deque()
Map = []
Map.append('@'*(W+2))
for i in range(H):
  c = list('@'+input()+'@')
  Map.append(c)
  for j in range(W+2):
    if(c[j] == '#'):
      Map[i+1][j] = 0
      by.append(i+1),bx.append(j)
Map.append('@'*(W+2))      

cnt = 0
while(1):
  if(len(by) == 0):
    break
   
  ny,nx = by.popleft(),bx.popleft()
  vec_y,vec_x = [1,-1,0,0],[0,0,1,-1]
  for i in range(4):
      if(Map[ny+vec_y[i]][nx+vec_x[i]] == '.'):
         Map[ny+vec_y[i]][nx+vec_x[i]] = Map[ny][nx] + 1
         cnt = max(cnt, Map[ny][nx] + 1) 
         by.append(ny+vec_y[i]),bx.append(nx+vec_x[i])
  
print(cnt)  