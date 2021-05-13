# 初期入力
A,B = (int(x) for x in input().split())

#
sukima =A-B*2
if 0 < sukima:
    print(sukima)
else:
    print(0)