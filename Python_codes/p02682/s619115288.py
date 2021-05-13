a,b,c,d=map(int, input().split())

if d<a:
  print(d)
elif d<b:
  print(a)
else:
  print(2*a-d+b)