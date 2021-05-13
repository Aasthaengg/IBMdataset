# input
S = input()

# check
yy, mm, dd = S.split("/")
if int(yy) >= 2019 and int(mm) >= 5:
    print("TBD")
else:
    print("Heisei")