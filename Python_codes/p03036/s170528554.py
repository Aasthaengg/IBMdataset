x=[0]*11
r,D,x[0]=map(int,input().split())
for i in range(1,11):
  x[i]=x[i-1]*r-D
  print(x[i])