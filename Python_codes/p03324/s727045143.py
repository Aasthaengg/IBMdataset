D,N=map(int,input().split())
p=0
if N==100:
  print(pow(100,D+1)+pow(100,D))
else:
  print(pow(100,D)*N)