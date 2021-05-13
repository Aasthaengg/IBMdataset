from collections import deque
h,w = map(int, input().split())
s = [input() for i in range(h)]
root = [[0,1],[1,0],[0,-1],[-1,0]]
def bfs(x,y):
  v[x][y]=1
  cnt=1
  cnt1=0
  d = deque([[x,y]])
  while len(d):
    e,f = d.popleft()
    c = s[e][f]
    for a,b in root:
      x1 = e+a
      y1 = f+b
      if x1>=0 and x1<h and y1>=0 and y1 <w and v[x1][y1]==0:
        if c == '.' and s[x1][y1]=='#':
          v[x1][y1]=1
          d.append([x1,y1])
          cnt+=1
        if c == '#' and s[x1][y1]=='.':
          v[x1][y1]=1
          d.append([x1,y1])
          cnt1+=1
  return cnt*cnt1
v = [[0 for i in range(w)] for j in range(h)]
ans=0
for i in range(h):
  for j in range(w):
    if v[i][j]:
      continue
    if s[i][j]=='#':
      ans+= bfs(i,j)
print(ans)