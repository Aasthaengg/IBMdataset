x,y = (int(x) for x in input().split())

z = x * y

if z % 2 == 0:
  print('Even')
  
else:
  print('Odd')