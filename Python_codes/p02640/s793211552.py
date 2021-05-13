x,y = map(int,input().split())


if y%2 != 0 or y > 4*x or y < 2*x:
  print('No')
else:
  print('Yes')