s = int(input())

a = s % 100
b = (s-a) / 100

if a >= 1 and a <= 12:
    if b >= 1 and b <= 12:
        print('AMBIGUOUS')
    else:
        print('YYMM')
else:
    if b >= 1 and b <= 12:
        print('MMYY')
    else:
        print('NA')