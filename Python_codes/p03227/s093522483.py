S = input()
if len(S) == 2:
  print(S)
else:
  t = ''
  for i in range(1, 4):
    t += S[-i]
  print(t)