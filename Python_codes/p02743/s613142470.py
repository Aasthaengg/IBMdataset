a,b,c = (int(x) for x in input().split())
if 4*a*b < (c-a-b)**2 and c-a-b > 0:
  print('Yes')
else:
  print('No')