s = int(input())
a = s//100
b = s%100
if 0 < b and b < 13 and 0 < a and a < 13:
    print("AMBIGUOUS")
elif 0 < b and b < 13:
    print("YYMM")
elif 0 < a and a < 13:
    print("MMYY")
else:
    print("NA")