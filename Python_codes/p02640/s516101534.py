x, y = map(int, input().split( ))
if x*2 > y or x*4 < y:
  print('No')
  exit()
dis = y - x*2
if dis%2==0:
  print('Yes')
else:
  print('No')
