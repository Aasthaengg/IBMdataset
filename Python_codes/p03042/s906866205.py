s = input()
a, b = s[:2], s[2:]
if '01' <= a <= '12':
    if '01' <= b <= '12':
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if '01' <= b <= '12':
        print('YYMM')
    else:
        print('NA')
