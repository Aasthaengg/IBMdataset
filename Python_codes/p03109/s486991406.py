import datetime
t = datetime.datetime.strptime("2019/04/30","%Y/%m/%d")
s = datetime.datetime.strptime(input(),"%Y/%m/%d")
print("Heisei") if t>=s else print("TBD")