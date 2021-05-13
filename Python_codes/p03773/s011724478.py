a,b = map(int,input().split())
h=a+b
if h>=24:
  print(h-24*(h//24))
else:
  print(h)