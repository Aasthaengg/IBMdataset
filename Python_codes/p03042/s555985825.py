S = input()
AS = S[:2]
BS = S[2:]
if 1<=int(AS)<=12 and 1<=int(BS)<=12:
    print('AMBIGUOUS')
elif 1<=int(AS)<=12:
    print('MMYY')
elif 1<=int(BS)<=12:
    print('YYMM')
else:
    print('NA')