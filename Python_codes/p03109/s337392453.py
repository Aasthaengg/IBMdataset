#!/usr/bin/env python3
import datetime
s = input()
tdatetime = datetime.datetime.strptime(s, '%Y/%m/%d')
tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
d = datetime.date(2019, 4, 30)
if tdate <= d:
    print('Heisei')
else:
    print('TBD')
