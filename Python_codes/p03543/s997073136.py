N = input()
s1 = set(list(N[1:]))
s2 = set(list(N[:-1]))
if len(s1) == 1 or len(s2) == 1:
  print('Yes')
else:
  print('No')