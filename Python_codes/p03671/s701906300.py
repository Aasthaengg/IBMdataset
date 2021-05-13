a,b,c=map(int,input().split())
if a+b<=a+c:
  print(min(a+b,b+c))
else:
  print(min(a+c,b+c))