s = input().split("/")
if int(s[0]) < 2019:
    print("Heisei")
elif int(s[0]) == 2019 and int(s[1]) < 4:
    print("Heisei")
elif int(s[0]) == 2019 and int(s[1]) == 4 and int(s[2]) <= 30:
    print("Heisei")
else:
    print("TBD")