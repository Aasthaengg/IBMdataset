from collections import deque
H,W = map(int,input().split())
L = []
for i in range(H):
  L.append(list(input()))
TF = []
for i in range(H):
  K = [False]*W
  TF.append(K)
dy_dx = [[1,0],[0,1],[-1,0],[0,-1]]
que = deque([[0,0]])
TF[0][0] = True
ans = 0
cntblack,cntwhite = 0,0
[cury,curx] = [0,0]
if L[0][0] == '#':
  cntblack += 1
else:
  cntwhite += 1
while [cury,curx] != [H-1,W-1]:
  if len(que) != 0:
    cur = que.popleft()
    TF[cur[0]][cur[1]] = True
    for i in range(4):
      if 0 <= cur[0]+dy_dx[i][0] <= H-1 and 0 <= cur[1]+dy_dx[i][1] <= W-1:
        if L[cur[0]+dy_dx[i][0]][cur[1]+dy_dx[i][1]] != L[cur[0]][cur[1]]:
          if TF[cur[0]+dy_dx[i][0]][cur[1]+dy_dx[i][1]] == False:
            TF[cur[0]+dy_dx[i][0]][cur[1]+dy_dx[i][1]] = True
            if L[cur[0]+dy_dx[i][0]][cur[1]+dy_dx[i][1]] == '#':
              cntblack += 1
            else:
              cntwhite += 1
            que.append([cur[0]+dy_dx[i][0],cur[1]+dy_dx[i][1]])
  else:
    ans += cntblack*cntwhite
    cntblack,cntwhite = 0,0
    if TF[cury][curx] == False:
      que.append([cury,curx])
      if L[cury][curx] == '#':
        cntblack += 1
      else:
        cntwhite += 1
    else:
      if curx != W-1:
        curx +=1
      elif cury != H-1:
        cury += 1
        curx = 0
      else:
        print(ans)
        exit()
print(ans)