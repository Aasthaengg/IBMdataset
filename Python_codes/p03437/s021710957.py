X,Y = map(int,input().split())
num = X
if X%Y==0:
  print(-1)
  exit()

while num <= 10**18:
  if num%Y != 0:
    print(num)
    exit()
  num += X
print(-1)