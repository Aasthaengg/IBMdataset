y, m, d= map(int, input().split('/'))
if int(str(y)+str(m).zfill(2)+str(d).zfill(2)) <= 20190430:
  print('Heisei')
else:
  print('TBD')