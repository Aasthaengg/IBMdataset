r,D,x2000=map(int,input().split())
check=x2000
for i in range(10):
  temp=r*check-D
  print(temp)
  check=temp
