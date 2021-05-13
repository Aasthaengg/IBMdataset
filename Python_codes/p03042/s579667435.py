S = input()
L = int(S[0:2])
R = int(S[2:4])
if 0 < L <= 12 and 0 < R <= 12:
    print("AMBIGUOUS")
elif 0 < L <= 12:
    print("MMYY")
elif 0 < R <= 12:
    print("YYMM")
else:
    print("NA")