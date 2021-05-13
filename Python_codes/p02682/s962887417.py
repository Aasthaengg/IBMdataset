a,b,c,d=map(int,input().split())
ans=0
if not a<d:
  print(d)
else:
  if not a+b<d:
    print(a)
  else:
    print(2*a+b-d)