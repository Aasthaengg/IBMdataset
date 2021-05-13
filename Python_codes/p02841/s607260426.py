# 初期入力　２０２０－０７２７　21：50
import sys
#input = sys.stdin.readline  #文字列では使わない
M1,D1 = map(int, input().split())
M2,D2 = map(int, input().split())

import datetime
import calendar
def get_last_date(dt):
    return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])

dt = datetime.datetime(2019, M1, D1)

if dt ==get_last_date(dt):
    print(1)
else:
    print(0)