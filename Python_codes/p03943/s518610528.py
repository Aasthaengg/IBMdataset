a,b,c=map(int,input().split())
d=max(a,b,c)
if((a+b+c-d)==d):
  print('Yes')
else:
  print('No')
