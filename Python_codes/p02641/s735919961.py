x,n = map(int,input().split())
if n>0:
  p = list(map(int,input().split()))
else:
  print(x)
  exit()
dx = 0
while True:
  if x-dx not in p:
    print(x-dx)
    exit()
  elif x+dx not in p:
    print(x+dx)
    exit()
  dx+=1