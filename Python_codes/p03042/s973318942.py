S = input()
l, r = int(S[:2]), int(S[2:])
if 0<l<13 and 0<r<13:
    print("AMBIGUOUS")
elif 0<l<13:
    print("MMYY")
elif 0<r<13:
    print("YYMM")
else:
    print("NA")
