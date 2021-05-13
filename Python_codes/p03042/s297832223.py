S = input()
if 1 <= int(S[:2]) <= 12 and not (1 <= int(S[2:]) <= 12):
    print('MMYY')
elif not (1 <= int(S[:2]) <= 12) and 1 <= int(S[2:]) <= 12:
    print('YYMM')
elif 1 <= int(S[:2]) <= 12 and 1 <= int(S[2:]) <= 12:
    print('AMBIGUOUS')
else:
    print('NA')