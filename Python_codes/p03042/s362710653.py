S=input()
if int(S[0]+S[1])>0 and int(S[0]+S[1])<13:
  if int(S[2]+S[3])>0 and int(S[2]+S[3])<13:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if int(S[2]+S[3])>0 and int(S[2]+S[3])<13:
    print("YYMM")
  else:
    print("NA")
 