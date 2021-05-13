a,b,c = map(int,input().split())

if a>=c:
  print(b+c)
else:
  c -= a
  if c<=b+1:
    print(a+c+b)
  else:
    print(a+b+b+1)