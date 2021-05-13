S = input()
mm = ["0"+str(x) for x in range(1,10)]+["10","11","12"]
mmyy = (S[:2] in mm)
yymm = (S[2:] in mm)
a = "NA"

if yymm and mmyy:
  a = "AMBIGUOUS"
elif yymm:
  a = "YYMM"
elif mmyy:
  a = "MMYY"
  
print(a)