# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
tstr =input().strip()
from datetime import datetime as dt

#tstr = '2012-12-29 13:49:37'
tdatetime = dt.strptime(tstr, '%Y/%m/%d')
standard ="2019/4/30"
dt_standard =dt.strptime(standard, '%Y/%m/%d')
if tdatetime <= dt_standard:
    print("Heisei")
else:
    print("TBD")