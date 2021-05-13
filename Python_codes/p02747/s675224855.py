S = input()
flg = True
if len(S)%2 == 1:
  print('No')
else:
  for i in range(0, len(S), 2):
    if S[i:i+2] != 'hi':
      print('No')
      flg = False
      break
  if flg:
    print('Yes')
  
