s = input()
bef = s[:2]
aft = s[2:]

if 1 <= int(bef) <= 12:
    if 1 <= int(aft) <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1 <= int(aft) <= 12:
        print("YYMM")
    else:
        print("NA")