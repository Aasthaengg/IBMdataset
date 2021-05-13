import datetime
s=input()
sd=datetime.datetime.strptime(s,"%Y/%m/%d")
st=datetime.datetime(2019,4,30)
if sd<=st:
    print("Heisei")
else:
    print("TBD")