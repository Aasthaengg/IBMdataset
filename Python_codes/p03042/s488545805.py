S = input()
if 0<int(S[0]+S[1])<13:	#MMかYY
  if 0<int(S[2]+S[3])<13:	#MMかYY
    print('AMBIGUOUS')
  else:	#YY
    print('MMYY')
else:	#YY
  if 0<int(S[2]+S[3])<13:	#MM
    print('YYMM')
  else:	#YY
    print('NA')