n,m=map(int,input().split())

c=n%m

if c<abs(c-m):
  print(c)
else:
  print(abs(c-m))