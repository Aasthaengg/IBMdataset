x = input()
pon = ['0', '1', '6', '8']
if x[-1] in pon:
  print('pon')
elif x[-1] == '3':
  print('bon')
else:
  print('hon')
