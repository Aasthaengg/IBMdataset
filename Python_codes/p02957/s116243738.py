a,b=map(int,input().split())
res = 0
c = a+b
if c % 2 == 1:
  print("IMPOSSIBLE")
else:
  res = int(c/2)
  print(res)