s=input()
if s[5:7] in ['01','02','03']:
  print('Heisei')
elif s[6:7] == '4' and int(s[-2:-1]) <= 30:
  print('Heisei')
else:
  print('TBD')
