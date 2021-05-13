[a,b,c,d] = list(map(int,input().split()))

flag=0
if abs(a-b)<=d:
  if abs(b-c)<=d:
    print('Yes')
  else:
    print('No')

elif abs(a-c)<=d:
  print('Yes')
else:
  print('No')

