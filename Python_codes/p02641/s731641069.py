x, n = map(int,input().split())
if n == 0:
  print(x)
  exit()
p = list(map(int,input().split()))
for i in range(100):
  if not x-i in p:
    print(x-i)
    break
  elif not x+i in p:
    print(x+i)
    break