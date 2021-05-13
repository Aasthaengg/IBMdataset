s = input()
mmyy = (1 <= int(s[:2]) <= 12)
yymm = (1 <= int(s[2:]) <= 12)
if mmyy:
  if yymm:
    print('AMBIGUOUS')
  else:
    print('MMYY')
else:
  if yymm:
    print('YYMM')
  else:
    print('NA')