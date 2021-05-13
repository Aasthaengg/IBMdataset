a,b,c  = input().split()
if a not in (b,c):
  print(a)
elif b not in (a,c):
  print(b)
else:
  print(c)