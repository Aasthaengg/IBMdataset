S = input()
S1 = []
for i in S:
  if i not in S1:
    S1.append(i)
if len(S1) == 2:
  print('Yes')
else:
  print('No')