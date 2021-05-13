a,b,c = map(int,input().split())

if a+b == c or abs(a-b) == c:
  print('Yes')
else:
  print('No')