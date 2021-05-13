S=input()
A=int(S[0:2])
B=int(S[2:4])
if (1<=A and A<=12) and (1<=B and B<=12):
  print("AMBIGUOUS")
elif (1<=A and A<=12) and not(1<=B and B<=12):
  print("MMYY")
elif not(1<=A and A<=12) and (1<=B and B<=12):
  print("YYMM")
else:
  print("NA")