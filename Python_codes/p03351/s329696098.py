a,b,c,d=[int(i) for i in input().split()]
T=abs(a-b)<=d and abs(b-c)<=d
if T or abs(a-c)<=d:
  print('Yes')
else:
  print('No')