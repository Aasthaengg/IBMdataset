import datetime

S = datetime.date(*map(int, input().split('/')))
x = datetime.date(2019, 4, 30)

print('Heisei' if S <= x else 'TBD')
