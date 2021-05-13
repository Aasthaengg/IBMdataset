S = input()
if (int(S[:2]) == 0 and (int(S[2:]) >= 13 or int(S[2:]) == 0)) or \
   (int(S[2:]) == 0 and (int(S[:2]) >= 13 or int(S[:2]) == 0)) or \
   (int(S[2:]) >= 13 and int(S[:2]) >= 13):
    print('NA')
elif (int(S[:2]) >= 13 and int(S[2:]) < 13) or \
     (int(S[:2]) == 0 and int(S[2:]) < 13):
    print('YYMM')
elif (int(S[2:]) >= 13 and int(S[:2]) < 13) or \
     (int(S[2:]) == 0 and int(S[:2]) < 13):
    print('MMYY')
else:
    print('AMBIGUOUS')
