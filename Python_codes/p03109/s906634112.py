import datetime
a,b,c = map(int,input().split("/"))
now = datetime.datetime(a,b,c)
d = now-datetime.datetime(2019,4,30)
print("TBD" if d.days > 0 else "Heisei")