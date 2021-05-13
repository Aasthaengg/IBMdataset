yyyy, mm, dd = input().split('/')
year = int(yyyy)
month = int(mm)
day = int(dd)
if year <= 2018:
  print('Heisei')
elif year == 2019:
  if month <= 3:
    print('Heisei')
  elif month == 4:
    print('Heisei')
  else:
    print('TBD')
else:
  print('TBD')