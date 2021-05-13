S = input()

if int(S[0:2]) > 12 or S[0:2] == "00":
    if 0 < int(S[2:4]) <= 12:
        print("YYMM")
    else:
        print("NA")
else:
    if 0 < int(S[2:4]) <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")