W,H,N = map(int,input().split())
L,R,D,U = 0,W,0,H

for i in range(N):
  x,y,a = map(int,input().split())
  if a==1:
    L=max(L,x)
  elif a==2:
    R=min(R,x)
  elif a==3:
    D=max(D,y)
  else:
    U=min(U,y)

print(max(0,R-L)*max(0,U-D))