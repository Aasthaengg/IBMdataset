from collections import deque
h,w = map(int, input().split())
s = [list('#'+input()+'#') for i in range(h)]
s = [['#']*(w+2)]+s+[['#']*(w+2)]
z=0
for i in s:
  z += i.count('.')
ans = [[-1]*(w+2) for i in range(h+2)]
m = [[0,1],[0,-1],[1,0],[-1,0]]
ans[1][1] = 1
d = deque([[1,1]])
while len(d):
  x,y = d.popleft()
  for i,j in m:
    a,b = x+i,y+j
    if s[a][b] == '.' and ans[a][b] == -1:
      d.append([a,b])
      ans[a][b] = ans[x][y]+1
if ans[h][w] == -1:
  print(-1)
else:
  print(z-ans[h][w])