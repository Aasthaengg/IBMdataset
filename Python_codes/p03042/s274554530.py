s = input()
n1 = int(s[0:2])
n2 = int(s[2:4])

if 1 <= n1 <= 12:
  if 1 <= n2 <= 12:
    print('AMBIGUOUS')
  else:
    print('MMYY')
elif 1 <= n2 <= 12:
  print('YYMM')
else:
  print('NA')
