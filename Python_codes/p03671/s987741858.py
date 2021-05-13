a,b,c = (int(x) for x in input().split())
if a+b <= a+c <= b+c or a+b <= b+c <= a+c:
  print (a+b)
elif a+c <= a+b <= b+c or a+c <= b+c <= a+b:
  print (a+c)
else:
  print (b+c)
