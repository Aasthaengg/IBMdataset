S = input()
high = int(S[0:2])
low = int(S[2:4])

if 1<= high <= 12:
    if 1<= low <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
if high < 1 or high > 12:
    if 1<= low <= 12:
        print("YYMM")
    else:
        print("NA")

