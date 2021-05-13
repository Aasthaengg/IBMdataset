import sys
N,Y=map(int,input().split())
Y=Y//1000
if N>Y or N*10<Y:
  print(-1,-1,-1)
  sys.exit()
for i in range(N+1):
  for j in range(N-i+1):
    k=N-i-j
    if i+5*j+10*k==Y:
      print(k,j,i)
      sys.exit()
print(-1,-1,-1)