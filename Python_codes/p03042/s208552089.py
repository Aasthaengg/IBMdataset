S = input()

if 0 < int(S[:2]) <= 12 and 0 < int(S[2:]) <= 12:
    print('AMBIGUOUS')
    exit()
elif 0 < int(S[:2]) <= 12:
    print('MMYY')
    exit()
elif 0 < int(S[2:]) <= 12:
    print('YYMM')
    exit()
else:
    print('NA')
    exit()
