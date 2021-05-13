n,m=map(int,input().split())
an=str(n)*m
am=str(m)*n

if an<am:
  print(an)
else:
  print(am)