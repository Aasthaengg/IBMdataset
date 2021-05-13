S=input()
months=['01','02','03','04','05','06','07','08','09','10','11','12']

if S[0:2] in months and S[2:4] in months:
    print('AMBIGUOUS')
elif S[0:2] in months:
    print('MMYY')
elif S[2:4] in months:
    print('YYMM')
else:
    print('NA')