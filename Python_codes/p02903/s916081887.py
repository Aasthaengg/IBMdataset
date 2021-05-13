H,W,A,B=map(int,input().split())
X=[0]*A+[1]*(W-A)
Y=[1]*A+[0]*(W-A)
for i in range(B):
  print(*X,sep='')
for i in range(H-B):
  print(*Y,sep='')