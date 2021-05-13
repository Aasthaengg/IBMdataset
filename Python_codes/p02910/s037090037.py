S = input()
ok = True
for i, s in enumerate(S):
  if not i % 2 and s == 'L':
    ok = False
    break
  if i % 2 and s == 'R':
    ok = False
    break
if ok:
  print('Yes')
else:
  print('No')