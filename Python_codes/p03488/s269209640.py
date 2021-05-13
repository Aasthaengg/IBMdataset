s=input()
x,y=map(int,input().split())
XY=[[]for i in range(2)]
a=0
b=0
for i in range(len(s)):
  if s[i]=="T":
    XY[b].append(a)
    a=0
    b=(b+1)%2
  else:
    a=a+1
XY[b].append(a)
xx=sum(XY[0])
yy=sum(XY[1])
dpx=[[0]*(2*xx+5) for i in range(len(XY[0])+1)]#x=0とj=xx+2を対応させる
dpy=[[0]*(2*yy+5) for i in range(len(XY[1])+1)]#y=0とj=yy+2を対応させる
dpx[1][xx+XY[0][0]+2]=1
for i in range(1,len(XY[0])):
  for j in range(2*xx+5):
    if dpx[i][j]==1:
      dpx[i+1][j-XY[0][i]]=1
      dpx[i+1][j+XY[0][i]]=1
dpy[0][yy+2]=1
for i in range(len(XY[1])):
  for j in range(2*yy+5):
    if dpy[i][j]==1:
      dpy[i+1][j-XY[1][i]]=1
      dpy[i+1][j+XY[1][i]]=1
if x+xx+2<0 or 2*xx+4<x+xx+2 or y+yy+2<0 or 2*yy+4<y+yy+2:
  print("No")
  exit()
if dpx[-1][x+xx+2]==1 and dpy[-1][y+yy+2]==1:
  print("Yes")
else:
  print("No")