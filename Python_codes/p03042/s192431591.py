s = input()
s1 = int(s[0:2])
s2 = int(s[2:])

if s1 > 0 and s1 < 13:
    if s2 > 0 and s2 < 13:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if s2 > 0 and s2 < 13:
        print("YYMM")
    else:
        print("NA")