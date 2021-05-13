from collections import deque

H, W = map(int, input().split())
Ss = []
for _ in range(H):
  Ss.append(input())

mp = [[0]*W for _ in range(H)]
dxy = [[-1,0],[1,0],[0,-1],[0,1]]
lst = []

q = deque([])
num = 1
for i in range(H):
  for j in range(W):
    if mp[i][j] == 0:
      q.append((i,j))
      mp[i][j] = num
      dic = {'#':0, '.':0}
      while q:
        t = q.popleft()
        dic[Ss[t[0]][t[1]]] += 1
        for k in range(4):
          if t[0] + dxy[k][0] >= 0 and t[0] + dxy[k][0] < H \
             and t[1] + dxy[k][1] >= 0 and t[1] + dxy[k][1] < W \
             and Ss[t[0]][t[1]] != Ss[t[0]+dxy[k][0]][t[1]+dxy[k][1]]\
             and mp[t[0]+dxy[k][0]][t[1]+dxy[k][1]] == 0:
            
            mp[t[0]+dxy[k][0]][t[1]+dxy[k][1]] = num
            q.append((t[0]+dxy[k][0],t[1]+dxy[k][1]))
      lst.append(dic)
      num += 1

rlt = 0
for d in lst:
  rlt += d['#']*d['.']

print(rlt)