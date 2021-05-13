import datetime as d
a,b = d.timedelta(seconds=int(input())),d.datetime(1,1,1)
print((a+b).hour, (a+b).minute, (a+b).second, sep=':')
