s = input()
m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
if s[:2] not in m and s[2:] not in m:
    print('NA')
elif s[:2] not in m:
    print('YYMM')
elif s[2:] not in m:
    print('MMYY')
else:
    print('AMBIGUOUS')