S = input()
o, x = 0, 0
for i in range(len(S)):
  if S[i] == 'o':
    o += 1
  elif S[i] == 'x':
    x += 1
if 15 - len(S) + o >= 8:
  print('YES')
else:
  print('NO')