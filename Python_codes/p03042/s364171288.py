s=input()
flag1=0
flag2=0
if 0<int(s[:2])<13:
  flag1=1
else:
  pass
if 0<int(s[2:])<13:
  flag2=1
else:
  pass

if flag1==0 and flag2==0:
  print("NA")
elif flag1==1 and flag2==0:
  print("MMYY")
elif flag1==0 and flag2==1:
  print("YYMM")
else:
  print("AMBIGUOUS")