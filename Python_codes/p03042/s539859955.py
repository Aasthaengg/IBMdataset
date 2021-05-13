s = input()
a,b = int(s[:2]),int(s[2:])
yymm = False
mmyy = False
if b > 0 and b <= 12:
  yymm = True
if a <= 12 and 0 < a:
  mmyy = True
if yymm and mmyy:
  print("AMBIGUOUS")
elif yymm:
  print("YYMM")
elif mmyy:
  print("MMYY")
else:
  print("NA")