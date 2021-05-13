S = input()

A = int(S[:2])
B = int(S[2:])

if  1 <= A and A <= 12:
    if  1 <= B and B <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if  1 <= B and B <= 12:
        print("YYMM")
    else:
        print("NA")
