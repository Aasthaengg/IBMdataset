S=[x for x in input()]
A='abcdefghijklmnopqrstuvwxyz'
for a in A:
  if a not in S:
    print(a)
    break
else:
  print('None')