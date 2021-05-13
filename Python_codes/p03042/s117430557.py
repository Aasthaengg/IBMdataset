s = input()

ym = 1 <= int(s[2:]) <= 12
my = 1 <= int(s[:2]) <= 12

if ym and my:
    print('AMBIGUOUS')
elif ym:
    print('YYMM')
elif my:
    print('MMYY')
else:
    print('NA')