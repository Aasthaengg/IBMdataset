from collections import deque
h,w = map(int,input().split())
l = [list(input()) for i in range(h)]
h1,w1= 0,0
#"."のかず
cou = 0
for i in l:
  for j in i:
    if j=='.':
      cou += 1
k = [[-1]*w for i in range(h)]
def bfs(a,b):
  d = deque()
  d.append([a,b])
  k[a][b]=0
  while d:
    c,e = d.popleft()
    m = [1,0,-1,0]
    n = [0,1,0,-1]
    for i in range(4):
      c1 = c+m[i]
      e1 = e+n[i]
      if 0<=c1 and 0<=e1 and c1<h and e1<w:
        if l[c1][e1]=="." and k[c1][e1]==-1:
          k[c1][e1]  =k[c][e] +1
          d.append([c1,e1])
  return k
bfs(h1,w1)        
if k[-1][-1]!=-1:
  print(cou-k[-1][-1]-1)
else:
  print(-1)