n=int(input())
x=0
y=0
t=0
fl=True
for i in range(n):
  nt,nx,ny=map(int,input().split())
  dist=abs(x-nx)+abs(y-ny)
  if (nt-t)%2!=dist%2 or (nt-t)<dist:
    print("No")
    break
  x,y=nx,ny
  t=nt
else:
  print("Yes")