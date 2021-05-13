S = int(input())

if 0 < S//100 < 13:
    if 0 < S%100 < 13:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if 0 < S%100 < 13:
        print('YYMM')
    else:
        print('NA')