import datetime

m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
'''
before = datetime.date(2019, m1, d1)
check = before + datetime.timedelta(day=1)

after = datetime.date(2019, m2, d2)
'''
if (m2 - m1 == 1):
    print(1)
else:
    print(0)
