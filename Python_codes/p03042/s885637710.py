s = input()
a, b = int(s[:2]), int(s[2:])
ym, my = False, False
if a > 0 and a <13:
    my = True
if b > 0 and b <13:
    ym = True
if ym and my:
    print('AMBIGUOUS')
elif ym and not my:
    print('YYMM')
elif not ym and my:
    print('MMYY')
else:
    print('NA')