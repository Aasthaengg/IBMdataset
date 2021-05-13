s = input()
if int(s[:4]) <= 2019:
  if int(s[5:7]) <= 4:
    if int(s[8:10]) <= 30:
      print('Heisei')
    else:
      print('TBD')
  else:
    print('TBD')
else:
  print('TBD')
