s = int(input())
f = s/100
l = s%100
if 1 <= f and f <= 12:
    if 1 <= l and l <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if 1 <= l and l <= 12:
        print('YYMM')
    else:
        print('NA')