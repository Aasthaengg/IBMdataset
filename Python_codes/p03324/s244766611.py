D,N=map(int,input().split())
if N<100:
  print(str(N)+str(0)*(D*2))
else:
  print(int(str(N)+str(0)*(D*2))+int(str(1)+str(0)*(D*2)))