w,h,n=map(int,input().split())
wx=[0]*w
hy=[0]*h
for i in range(n):
  x,y,a=map(int,input().split())
  x-=1
  y-=1
  if a==1:
    for j in range(x+1):
      wx[j]=1
  if a==2:
    for j in range(x+1,w):
      wx[j]=1
  if a==3:
    for j in range(y+1):
      hy[j]=1
  if a==4:
    for j in range(y+1,h):
      hy[j]=1
print(wx.count(0)*hy.count(0))
#print(wx)
#print(hy)