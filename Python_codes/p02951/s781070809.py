a,b,c = map(int,input().split())
r = c - a + b
if r < 0:
  print(0)
else:
  print(r)