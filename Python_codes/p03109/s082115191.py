import datetime
S=input()
dte = datetime.datetime.strptime(S, '%Y/%m/%d')
deh = datetime.datetime.strptime("2019/04/30",'%Y/%m/%d')
if dte<=deh:
  print("Heisei")
else:
  print("TBD")