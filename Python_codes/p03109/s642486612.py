S = input().rstrip()
if int(S[:4]) >=2020:
    print("TBD")
    exit()
elif int(S[:4]) ==2019:
    if int(S[5:7]) >= 5:
        print("TBD")
        exit()
    elif int(S[5:7]) >= 4:
        if int(S[8:]) >= 31:
            print("TBD")
            exit()
print("Heisei")