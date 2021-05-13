from datetime import datetime as dt
s = input()
s = dt.strptime(s, '%Y/%m/%d')
cm = dt.strptime("2019/4/30", '%Y/%m/%d')
# print((s-cm).days)
if (s-cm).days > 0:
    print("TBD")
else:
    print("Heisei")
