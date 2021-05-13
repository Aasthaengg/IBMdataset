S = input()
f = int(S[:2])
b = int(S[2:])
if (not 0 < f <= 12) and 0 < b <= 12:
    print('YYMM')
elif (not 0 < b <= 12) and 0 < f <= 12:
    print('MMYY')
elif 0 < f <= 12 and 0 < b <= 12:
    print('AMBIGUOUS')
else:
    print('NA')
