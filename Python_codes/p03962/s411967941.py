a,b,c=map(int,input().split())

if a==b and b==c:
  print(1)
elif (a==b and b!=c) or (b==c and c!=a) or (c==a and a!=b):
  print(2)
else:
  print(3)