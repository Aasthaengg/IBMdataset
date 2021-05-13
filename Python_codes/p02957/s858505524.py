n,m = (int(x) for x in input().split())
if n%2 != m%2:
  print('IMPOSSIBLE')
else:
  print(int((n+m)/2))