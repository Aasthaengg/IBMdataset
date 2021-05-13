x=int(input())
f=x//100
d=x%100
ff=bool(1)
dd=bool(1)
if f==0 or f>12:
  ff=0
if d==0 or d>12:
  dd=0

if ff==1 and dd==1:
  print("AMBIGUOUS")
elif ff==0 and dd==0:
  print("NA")
else:
  if ff==1 and dd==0:
    print("MMYY")
  else:
    print("YYMM")