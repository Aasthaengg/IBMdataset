a,b = map(int, open(0).read().split())
if (a+b) <24:
  print(a+b)
else:
  print((a+b)%24)