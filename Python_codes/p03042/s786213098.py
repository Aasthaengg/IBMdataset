from sys import exit
S = input()

if 0 < int(S[0:2]) < 13:
    if 0 < int(S[2:]) < 13:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 0 < int(S[2:]) < 13:
        print("YYMM")
    else:
        print("NA")