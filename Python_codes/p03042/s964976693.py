s = input()
a = int(s[:2])
b = int(s[2:])
if 0 < a and a<13:
    if 0<b and b<13:
        print('AMBIGUOUS')
    else:
        print('MMYY')
elif 0<b and b<13:
    print('YYMM')
else:
    print('NA')