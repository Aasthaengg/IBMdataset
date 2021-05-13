
import datetime
import calendar

m1,d1 = map(int,input().split())
m2,d2 = map(int,input().split())

day1 = datetime.date(2019, m1, d1)
day2 = datetime.date(2019, m1, calendar.monthrange(2019, m1)[1])

if day1 == day2:
    print("1")
else:
    print("0")