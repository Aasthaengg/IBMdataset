s = input()
year = s[0:4]
month = s[5:7]
day = s[8:10]
i = int(year + month + day)
if i <= 20190430:
  print('Heisei')
else:
  print('TBD')