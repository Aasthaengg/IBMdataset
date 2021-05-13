import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限

import datetime
chk = datetime.datetime.strptime("2019/5/1","%Y/%m/%d")
s   = datetime.datetime.strptime(input(),"%Y/%m/%d")
if s<chk:
    print("Heisei")
else:
    print("TBD")