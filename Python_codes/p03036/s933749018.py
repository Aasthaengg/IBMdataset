r,d,x=map(int,input().split())
ans=[0]*10
for i in range(10):
  x=r*x-d
  print(x)