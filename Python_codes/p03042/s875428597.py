S = input()
n1 = int(S[:2])
n2 = int(S[2:])

if 1 <= n1 <= 12 and 1 <= n2 <= 12:
    print('AMBIGUOUS')
elif 1 <= n1 <= 12 and (not 1 <= n2 <= 12):
    print('MMYY')
elif (not 1 <= n1 <= 12) and 1 <= n2 <= 12:
    print('YYMM')
else:
    print('NA')
