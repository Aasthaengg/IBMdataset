s = sorted(list(input()))
t = sorted(list(input()), reverse=True)
if s == t:
  print('No')
else:
  c = sorted([s, t])
  if c[0] == s:
    print('Yes')
  else:
    print('No')