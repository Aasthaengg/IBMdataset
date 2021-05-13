x, n = map(int,input().split())
if n != 0:
  p = list(map(int,input().split()))
else:
  print(x)
  exit()

for j in range(100):
  if all(x-j != i for i in p):
    print(x-j)
    exit()
  elif all(x+j != i for i in p):
    print(x+j)
    exit()