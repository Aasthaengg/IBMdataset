import datetime
year,month,day = map(int, input().split("/"))
comp1 = datetime.datetime(year, month, day, 0, 0, 0)
comp2 = datetime.datetime(2019, 4, 30, 0, 0, 0)
print("Heisei" if (comp1 <= comp2) else "TBD")
