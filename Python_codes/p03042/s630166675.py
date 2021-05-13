S = list(input())
S1 = S[0] + S[1]
S2 = S[2] + S[3]
S1 = int(S1)
S2 = int(S2)

if 1 <= S1 <= 12 and 1 <= S2 <= 12:
  print('AMBIGUOUS')
elif (1 > S1 or S1 > 12) and 1 <= S2 <= 12:
  print('YYMM')
elif (1 > S2 or S2 > 12) and 1 <= S1 <= 12:
  print('MMYY')
else:
  print('NA')
