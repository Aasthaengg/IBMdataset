S = input()
count = 0
for s in S:
  if s == 'o':
    count += 1
if count + (15 - len(S)) >= 8:
  print('YES')
else:
  print('NO')