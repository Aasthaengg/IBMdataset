S = input()
C = []
f = True
for s in S:
  if s not in C:
    C.append(s)
  else:
    f = False
print('yes' if f else 'no')