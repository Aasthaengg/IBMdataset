a,b=map(int,input().split())
c=int(str(a)*b)
d=int(str(b)*a)
if c>d:
  print(str(a)*b)
else:
  print(str(b)*a)
