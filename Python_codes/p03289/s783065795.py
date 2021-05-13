S = input()
abc = 'abcdefghijklmnopqrstuvwxyz'
if S[0] == 'A':
  if S[2:len(S)-1].count('C') == 1:
    for c in S:
      if (c!='A') and (c!='C') and (c not in abc):
        print('WA')
        exit()
    else:
      print('AC')
  else:
    print('WA')
else:
  print('WA')