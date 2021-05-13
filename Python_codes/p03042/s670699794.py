S = input()
if (int(S[:2])>12 or int(S[:2])==0) and (int(S[2:])>12 or int(S[2:])==0):
    print('NA')
elif (int(S[:2])<=12 and int(S[:2])!=0) and (int(S[2:])>12 or int(S[2:])==0):
    print('MMYY')
elif (int(S[2:])<=12 and int(S[2:])!=0) and (int(S[:2])>12 or int(S[:2])==0):
    print('YYMM')
else:
    print('AMBIGUOUS')