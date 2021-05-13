y,m,d=[int(x) for x in input().split('/')]
if y < 2019:
  print('Heisei')
elif y > 2019:
  print('TBD')
elif m <= 4:
  print('Heisei')
elif m > 4:
  print('TBD')