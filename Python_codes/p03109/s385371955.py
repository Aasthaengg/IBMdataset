import datetime


s = input()

target = datetime.datetime.strptime(s, '%Y/%m/%d')
heisei = datetime.datetime(2019, 4, 30)


if (target - heisei).days <= 0:
    print('Heisei')
else:
    print('TBD')
