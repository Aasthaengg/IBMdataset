s = input()
if len(s) % 2 != 0:
  print('No')
  exit()
for t in s[::2]:
  if t != 'h':
    print('No')
    exit()
for t in s[1::2]:
  if t != 'i':
    print('No')
    exit()
print('Yes')