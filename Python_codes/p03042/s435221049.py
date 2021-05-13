s=input()
ym=True if 0 < int(s[2:]) < 13 else False
my=True if 0 < int(s[:2]) < 13 else False
if my and ym:
  print('AMBIGUOUS')
elif my:
  print('MMYY')
elif ym:
  print('YYMM')
else:
  print('NA')