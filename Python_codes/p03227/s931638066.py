s = list(input())
if len(s) == 2:
  print(''.join(s))
else:
  s[0], s[2] = s[2], s[0]
  print(''.join(s))