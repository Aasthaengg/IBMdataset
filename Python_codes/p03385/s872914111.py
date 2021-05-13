S=input()
flagA = False
flagB = False
flagC = False
for i in range(3):
  if S[i] == "a":
    flagA = True
  elif S[i] == "b":
    flagB = True
  elif S[i] == "c":
    flagC = True
  else:
    pass
if flagA and flagB and flagC:
  print("Yes")
else:
  print("No")