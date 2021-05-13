s = input()
a = int(s[:2])
b = int(s[2:])

if 0 < a < 13:
    if 0 < b < 13:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 0 < b < 13:
        print('YYMM')
    else:
        print('NA')