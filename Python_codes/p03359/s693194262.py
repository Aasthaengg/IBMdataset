from datetime import date, timedelta

a, b = map(int, input().split())
d1 = date(year=2018, month=1, day=1)
d2 = date(year=2018, month=a, day=b)

count = 0
while d1 <= d2:
    if d1.month == d1.day:
        count += 1
    d1 += timedelta(days=1)

print(count)
