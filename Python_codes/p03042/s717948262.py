S = input()
sform = int(S[:2])
slatt = int(S[2:])

if sform <= 12 and sform >= 1:
    if slatt <= 12 and slatt >= 1:
        print('AMBIGUOUS')
    else:
        print('MMYY')

else:
    if slatt <= 12 and slatt >= 1:
        print('YYMM')
    else:
        print('NA')