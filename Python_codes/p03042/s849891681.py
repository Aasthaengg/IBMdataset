s = input()
a, b = int(s[:2]), int(s[2:])

if 1<=a<=12 and 1<=b<=12:
  print('AMBIGUOUS')
elif 1<=b<=12:
  print('YYMM')
elif 1<=a<=12:
  print('MMYY')
else:
  print('NA')