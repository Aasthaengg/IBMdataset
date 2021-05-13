num = list(map(int, input()))

if ((num[-1] == 0) or (num[-1] == 1) or (num[-1] == 6) or (num[-1] == 8)):
    print("pon")
elif num[-1] == 3:
    print("bon")
else:
    print("hon")