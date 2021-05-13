a = input()
if int(a[:2]) < 13 and int(a[:2]) > 0:
    if int(a[2:4]) < 13 and int(a[2:4]) > 0: print('AMBIGUOUS')
    else: print('MMYY')
elif int(a[2:]) < 13 and int(a[2:]) > 0: print('YYMM')
else: print('NA')