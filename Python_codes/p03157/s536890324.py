import sys;sys.setrecursionlimit(10**9)
h,w=map(int,input().split())
b=[[0]*(w+1)]
for i in range(h):
  b.append([0])
  for j in input():
    if j==".":b[-1].append(1)
    else:b[-1].append(2)
  b[-1].append(0)
b.append([0]*(w+1))
d=[[0,1],[0,-1],[1,0],[-1,0]]
a=0
def bfs(i,j):
  global br,wh
  if b[i][j]==0:return
  if b[i][j]==1:wh+=1
  elif b[i][j]==2:br+=1
  v=b[i][j]
  b[i][j]=0
  for k in d:
    if v^3!=b[i+k[0]][j+k[1]]:continue
    bfs(i+k[0],j+k[1])
for i in range(1,h+1):
  for j in range(1,w+1):
    br=wh=0
    bfs(i,j)
    a+=br*wh
print(a)