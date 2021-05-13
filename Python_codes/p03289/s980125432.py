S = list(input())

if S[0] == 'A':
  isC = 0
  for i in S[2:len(S)-1]:
    if i == 'C':
      isC += 1
  else:
    if isC == 1:
      for i in range(len(S)):
        if S[i] == 'A' or S[i] =='C' or S[i].islower():
          pass
        else:
          print('WA')
          break
      else:
        print('AC')
    else:
      print('WA')
else:
  print('WA')