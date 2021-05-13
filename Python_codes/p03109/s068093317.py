import datetime

dt = datetime.datetime.strptime(input(), '%Y/%m/%d')
print('Heisei' if dt <= datetime.datetime(2019, 4, 30) else 'TBD')
