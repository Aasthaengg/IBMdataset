S = input()
A = int(S[0] + S[1])
B = int(S[2] + S[3])

if 1 <= A <= 12 and 1 <= B <= 12:
    print('AMBIGUOUS')
elif (A > 12 or A <= 0) and 1 <= B <= 12:
    print('YYMM')
elif 1 <= A <= 12 and (B > 12 or B <= 0):
    print('MMYY')
else:
    print('NA')
