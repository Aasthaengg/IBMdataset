b = input()
AT = ["A", "T"]
CG = ["C", "G"]

if b in AT:
  AT.remove(b)
  print(AT[0])
else:
  CG.remove(b)
  print(CG[0])