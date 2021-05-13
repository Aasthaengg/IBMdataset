W,H,N=map(int,input().split())
d=[]
for i in range(H):
  d.append([1]*W)
for j in range(N):
  x,y,a=map(int,input().split())
  if a==1:
    for i1 in range(H):
      for x1 in range(x):
        d[i1][x1]=0
  elif a==2:
    for i2 in range(H):
      for x2 in range(x,W):
        d[i2][x2]=0
  elif a==3:
    for i3 in range(y):
      for y1 in range(W):
        d[i3][y1]=0
  else:
    for i4 in range(y,H):
      for y2 in range(W):
        d[i4][y2]=0
ans=0
for k in d:
  ans+=sum(k)
print(ans)
