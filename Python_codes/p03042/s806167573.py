S = input()
S1, S2 = S[0:2], S[2:5]
if (int(S1) >= 1 and int(S1) <=12) and (int(S2) >= 1 and int(S2) <=12):
	print('AMBIGUOUS')
elif int(S2) >= 1 and int(S2) <= 12:
	print('YYMM')
elif int(S1) >= 1 and int(S1) <=12:
	print('MMYY')
else:
	print('NA')

