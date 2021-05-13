s = input()
for i in range(len(s)):
  if i & 1 == 0:
    if s[i] != 'h':
      break
  else:
    if s[i] != 'i':
      break
else:
  if len(s) & 1 == 0:
    print('Yes')
    exit()
print('No')
