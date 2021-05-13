x,a,b = (int(x) for x in input().split())

if abs(x-a) > abs(x-b):
  print('B')
elif abs(x-a) < abs(x-b):
  print('A')