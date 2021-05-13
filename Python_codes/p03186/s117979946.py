a,b,c=map(int,input().split())
if c<=b:
  print(c+b)
else:
  if c-b<=a:
    print(c+b)
  else:
    print(a+b+b+1)