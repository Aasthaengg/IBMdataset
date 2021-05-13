a,b,c=map(int,input().split())
d=max(a,b,c)
if d == a+b+c-d:
  print('Yes')
else:
  print('No')