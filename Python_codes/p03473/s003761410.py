import datetime

M = int(input())
today = datetime.datetime(2019, 12, 30, M)
new_year = datetime.datetime(2020, 1, 1, 0)
td = new_year - today

print(td.days * 24 + td.seconds // 3600)
