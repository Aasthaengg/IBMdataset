S = input()
if ord(S[0]) != 65:
  print('WA')
else:
  b = 0
  c = 0
  for i in range(1, len(S)):
    if i != 1 and i != len(S) - 1 and ord(S[i]) == 67:
      b += 1
    elif ord(S[i]) <= 96 or 123 <= ord(S[i]):
      c = 1
  if b == 1 and c == 0:
    print('AC')
  else:
    print('WA')