s=input()
a=int(s[:2])
b=int(s[2:])
ac=0
bc=0
if 0<a and a<13:
  ac=1
if 0<b and b<13:
  bc=1
  
if ac and bc:
  print("AMBIGUOUS")
elif ac:
  print("MMYY")
elif bc:
  print("YYMM")
else:
  print("NA")