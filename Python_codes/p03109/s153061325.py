import datetime as dt
S=input()
s=dt.datetime.strptime(S,'%Y/%m/%d')
A='2019/04/30'
a=dt.datetime.strptime(A,'%Y/%m/%d')
if s<=a:
    print('Heisei')
else:
    print('TBD')
