a,b,c=map(int,input().split())
if a*c <= b:
  print(c)
elif a*c >= b:
  print(b//a)
else:
  print(0)