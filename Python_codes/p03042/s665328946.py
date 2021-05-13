s = (input())
a= s[0:2]
b= s[2:4]
a = int(a)
b= int(b)
if a == 0 or b == 0:
  if b!= 0 and b<13:
    print('YYMM')
  elif a!= 0 and a<13:
    print('MMYY')
  else:
    print('NA')
elif a<13 or b<13:
  if a>12:
    print('YYMM')
  elif b>12:
    print('MMYY')
  else:
    print('AMBIGUOUS')
else:
  print('NA')