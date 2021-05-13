s = input()
if s[0] == 'A':
  t = ''
  c_cnt = 0
  for i in range(1, len(s)):
    if s[i] != 'C':
      t += s[i]
    else:
      c_cnt += 1
  if t.islower() and 'C' in s[2:-1] and c_cnt == 1:
    print('AC')
  else:
    print('WA')
else:
  print('WA')
