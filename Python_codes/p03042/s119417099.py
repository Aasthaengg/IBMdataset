s = input()

x = int(s[:2])
y = int(s[2:])

if 1 <= x <= 12 and 1 <= y <= 12:
    print("AMBIGUOUS")
elif 1 <= x <= 12:
    print("MMYY")
elif 1 <= y <= 12:
    print("YYMM")
else:
    print('NA')