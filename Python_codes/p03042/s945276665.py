S = input()
f = int(S[:2])
s = int(S[2:])
if 1 <= f <= 12 and 1 <= s <= 12:
    print('AMBIGUOUS')
elif 1 <= f <= 12:
    print('MMYY')
elif 1 <= s <= 12:
    print('YYMM')
else:
    print('NA')