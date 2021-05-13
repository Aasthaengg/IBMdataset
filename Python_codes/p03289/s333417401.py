S = input()
CS = S[2:-1]
if S[0] == 'A':
  S = S.lstrip('A')
  if CS.count('C') == 1:
    S = S.replace('C', '')
    if S.islower() == True:
      print('AC')
    else:
      print('WA')
  else:
    print('WA')
else:
  print('WA')