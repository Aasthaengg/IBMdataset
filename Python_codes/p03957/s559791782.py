s = input()
if not 'C' in s:
  print('No')
else:
  c = s.find('C')
  s = s[c:]
  if 'F' in s:
    print('Yes')
  else:
    print('No')