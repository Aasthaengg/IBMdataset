s = input()

a, b = int(s[:2]), int(s[2:])
if 0 < a < 13 and 0 < b < 13:
    print('AMBIGUOUS')
elif 0 < a < 13:
    print('MMYY')
elif 0 < b < 13:
    print('YYMM')
else:
    print("NA")
