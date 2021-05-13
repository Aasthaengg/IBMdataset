from datetime import datetime
s=input()
sdate=datetime.strptime(s,"%Y/%m/%d")
cdate=datetime.strptime("2019/04/30","%Y/%m/%d")
print("Heisei" if sdate<=cdate else "TBD")