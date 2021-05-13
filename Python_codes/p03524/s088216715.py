S = input()
c_a = 0
c_b = 0
c_c = 0
for i in range(len(S)):
  if S[i] == 'a':
    c_a += 1
  elif S[i] == 'b':
    c_b += 1
  else:
    c_c += 1
if abs(c_a -c_b) < 2 and abs(c_b - c_c) < 2 and abs(c_c - c_a) < 2:
  print('YES')
else:
  print('NO')