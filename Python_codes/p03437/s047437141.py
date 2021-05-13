X,Y=map(int,input().split())
if X%Y==0:
  print(-1)
  exit()
  
i = 2
while True:
  if X*i % Y != 0 and X*i <= 10**18:
    print(X*i)
    exit()
  i += 1
  if X*i > 10**18:
    print(-1)
    exit()