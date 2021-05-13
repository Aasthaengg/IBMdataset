x = list(map(int, input().split("/")))
if x[0] > 2019:
    print("TBD")
    exit()
elif x[0] == 2019:
    if x[1] > 4:
        print("TBD")
        exit()
    elif x[1] == 4:
        if x[2] > 30:
            print("TBD")
            exit()
        else:
            print("Heisei")
            exit()
    else:
        print("Heisei")
        exit()
else:
    print("Heisei")
    exit()
