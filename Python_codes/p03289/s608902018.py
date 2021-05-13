S = input()
if S[0] != 'A':
  print('WA')
elif S[2:-1].count('C') != 1:
  print('WA')
else:
  cindex = S.index('C')
  for i in range(len(S[1:])):
    if i+1 == cindex:
      continue
    if S[i+1].isupper():
      print('WA')
      exit()
  print('AC')
