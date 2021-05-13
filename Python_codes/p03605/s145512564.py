n = input()
l = 0
for i in range(len(n)):
  if n[i] == '9':
    l += 1
if l > 0:
  print('Yes')
else:
  print('No')