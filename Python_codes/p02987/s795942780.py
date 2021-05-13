import collections

S = input()

c = collections.Counter(S)


if len(c.values()) == 2:
  a, b = c.values()
  if a == b:
    print('Yes')
  else:
    print('No')
else:
  print('No')