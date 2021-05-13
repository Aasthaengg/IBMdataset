S = list(input())

a = int("".join(S[0:2]))
b = int("".join(S[2:4]))

if 1 <= a <= 12 and 1 <= b <= 12:
    print("AMBIGUOUS")
elif 1 <= a <= 12:
    print("MMYY")
elif 1 <= b <= 12:
    print("YYMM")
else:
    print("NA")
