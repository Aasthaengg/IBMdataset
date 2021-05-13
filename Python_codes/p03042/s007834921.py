s = str(input())
A = int(s[0:2]); B = int(s[2:4])
if 1 <= A <= 12 and 1 <= B <= 12:
    print("AMBIGUOUS")
elif 1 <= A <= 12 and 0 <= B <= 99:
    print("MMYY")
elif 1 <= B <= 12 and 0 <= A <= 99:
    print("YYMM")
else:
    print("NA")