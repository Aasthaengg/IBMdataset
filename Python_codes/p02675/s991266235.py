n = input()

i = n[-1]
i = int(i)
if i == 3:
  print('bon')
elif i == 0 or i == 1 or i == 6 or i == 8:
  print('pon')
else:
  print('hon')