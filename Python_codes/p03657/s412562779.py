a,b = map(int,input().split())
if a%3 == b%3 == 1 or a%3 == b%3 == 2:
  print('Impossible')
else:
  print('Possible')