S = input()
A = int(S[:2])
B = int(S[2:])

if 1<=A<=12 and 1<=B<=12:
  print("AMBIGUOUS")
elif 1<=A<=12:
  print("MMYY")
elif 1<=B<=12:
  print("YYMM")
else:
  print("NA")