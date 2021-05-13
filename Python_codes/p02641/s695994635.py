x,n = map(int,input().split())

if n == 0:
  print(x)
  exit()

p = list(map(int,input().split()))

if x not in p:
  print(x)
  exit()

x1,x2 = x,x
for i in range(100):
  x1 -= 1
  x2 += 1
  if x1 not in p:
    print(x1)
    exit()
  if x2 not in p:
    print(x2)
    exit()