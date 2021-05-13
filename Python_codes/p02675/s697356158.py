N=input()
hon=str('24579')
pon=str('0168')
if N[-1] in hon:
  print('hon')
elif N[-1] in pon:
  print('pon')
else:
  print('bon')