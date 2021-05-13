s=input()
year=s[:4]
month=s[5:7]
day=s[8:]
s2=int(year+month+day)
if s2<=20190430:
    print("Heisei")
else:
    print("TBD")