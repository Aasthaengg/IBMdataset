S = input()
months = [i for i in range(1, 13)]
left = int(S[:2])
right = int(S[2:])
if left in months and right in months:
    print('AMBIGUOUS')
elif left in months:
    print('MMYY')
elif right in months:
    print('YYMM')
else:
    print('NA')