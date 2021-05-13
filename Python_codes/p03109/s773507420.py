s = input()
year = int(s[:4])
month = int(s[5:7])
day = int(s[9:])
if year > 2019:
  print('TBD')
elif year < 2019:
  print('Heisei')
else:
  if month > 4:
    print('TBD')
  elif month < 4:
    print('Heisei')
  else:
    if day > 30:
      print('TBD')
    else:
      print('Heisei')
