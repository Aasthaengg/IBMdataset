S = input()
if int(S[0: 2]) >= 13 or int(S[0: 2]) == 0:
    if int(S[2: 4]) == 0 or int(S[2: 4]) >= 13:
        print('NA')
    else:
        print('YYMM')
else:
    if int(S[2: 4]) == 0 or int(S[2: 4]) >= 13:
        print('MMYY')
    else:
        print('AMBIGUOUS')