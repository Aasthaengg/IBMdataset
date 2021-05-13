l = [int(x) for x in input().split(' ')]
if abs(l[0]-l[1]) < abs(l[0]-l[2]):
  print('A')
else:
  print('B')