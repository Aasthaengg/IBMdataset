a,b,c=map(int,input().split())
x=4*a*b
y=(c-a-b)*(c-a-b)
if c-a-b<0:
  print('No')
else:
  
  if x<y:
    print('Yes')
  else:
    print('No')