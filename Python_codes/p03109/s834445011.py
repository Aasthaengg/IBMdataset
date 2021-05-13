from datetime import datetime as dt
tstr = input()
tdatetime  = dt.strptime(tstr, '%Y/%m/%d')
tstr = '2019/04/30'
heiseitime = dt.strptime(tstr, '%Y/%m/%d')
if heiseitime >= tdatetime:
  print("Heisei")
else:
  print("TBD")