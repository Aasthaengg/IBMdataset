s = sorted(list(input()))
for i in range(len(s) - 1):
  if s[i] == s[i + 1]:
    print('no')
    break
else:
  print('yes')
