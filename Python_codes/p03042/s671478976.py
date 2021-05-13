s=input()

first_two=int(''.join(s[:2]))
last_two=int(''.join(s[2:]))

if 1<=first_two<=12 and 1<=last_two<=12:
  print('AMBIGUOUS')
elif 1<=last_two<=12:
  print('YYMM')
elif 1<=first_two<=12:
  print('MMYY')
else:
  print('NA')