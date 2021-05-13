YYMM = False
MMYY = False
f = input()
h1 = f[0] + f[1]
h2 = f[2] + f[3]

if 1 <= int(h2) <= 12:
  YYMM = True
if 1 <= int(h1) <= 12:
  MMYY = True

def ret(c1,c2):
  if c1 and c2:
    return "AMBIGUOUS"
  elif c1:
    return "YYMM"
  elif c2:
    return "MMYY"
  else:
    return "NA"
  
print(ret(YYMM,MMYY))