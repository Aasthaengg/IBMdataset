S = input()
strs = list(reversed(S))
rev_S = ''.join(strs)
while True:
  if rev_S[:6] == 'resare':
    rev_S = rev_S[6:]
    continue
  elif rev_S[:7] == 'remaerd':
    rev_S = rev_S[7:]
    continue
  elif rev_S[:5] == 'esare' or rev_S[:5] == 'maerd':
    rev_S = rev_S[5:]
    continue
  else:
    break

if rev_S == '':
  print('YES')
else:
  print('NO')

