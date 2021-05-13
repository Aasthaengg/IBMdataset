s = input()
upper_input = int(s[:2])
lower_input = int(s[2:])

if upper_input >= 1 and upper_input<= 12:
  if lower_input >= 1 and lower_input <= 12:
    print('AMBIGUOUS')
  else:
    print('MMYY')
else:
  if lower_input >= 1 and lower_input <= 12:
    print('YYMM')
  else:
    print('NA')