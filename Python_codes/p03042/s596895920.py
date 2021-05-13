s = input()
yymm = 1 <= int(s[2:]) <= 12
mmyy = 1 <= int(s[:2]) <= 12
if yymm and mmyy:
    print('AMBIGUOUS')
elif yymm:
    print('YYMM')
elif mmyy:
    print('MMYY')
else:
    print('NA')