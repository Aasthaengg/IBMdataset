import datetime
s = input().split("/")
if datetime.date(2019,4,30) >= datetime.date(int(s[0]), int(s[1]), int(s[2])):
    print('Heisei')
else:
    print('TBD')