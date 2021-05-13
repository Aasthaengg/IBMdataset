S = input()
flagA = False
flagB = False
if 1 <= int(S[2:4])<= 12:
  flagB = True
if 1 <= int(S[0:2])<= 12:
  flagA = True
if flagA and flagB:
  print("AMBIGUOUS")
elif flagA and not flagB:
  print("MMYY")
elif flagB and not flagA:
  print("YYMM")
else:
  print("NA")