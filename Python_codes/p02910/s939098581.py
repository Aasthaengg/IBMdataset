S = input()
result = False
for s in S[::2]:
  if s not in 'RUD':
    break
else:
  for s in S[1::2]:
    if s not in 'LUD':
      break
  else:
    result = True
print('Yes' if result else 'No')  