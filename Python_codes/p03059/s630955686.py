a,b,t = map(int,input().split())
if a > t:
  print(0)
else:
  L = t // a
  print(L*b)