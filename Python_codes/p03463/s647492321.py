n,a,b = map(int, input().split())
if n == 2:
  print('Borys')
elif a == 1 and b == 2:
  print('Borys')
elif (a - b) % 2 == 0:
  print('Alice')
else:
  print('Borys')