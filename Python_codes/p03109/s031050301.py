y, m, d = map(int, input().split("/"))

if y < 2019:
    print("TBD")
elif y == 2019:
    if m >= 5:
        print("TBD")
    else:
        print("Heisei")
else:
    print("Heisei")