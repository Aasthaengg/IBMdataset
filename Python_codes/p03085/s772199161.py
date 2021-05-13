at = "AT"
cg = "CG"
b = input()

if at.count(b) == 1:
  print(str(at.strip(b)))
else:
  print(str(cg.strip(b)))