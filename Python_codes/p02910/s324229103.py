s = input()
count = 0
for i in range(len(s)):
  if i % 2 != 0 and (s[i] == 'L' or s[i] == 'U' or s[i] == 'D'):
    count += 1
  elif i % 2 == 0 and (s[i] == 'R' or s[i] == 'U' or s[i] == 'D'):
    count += 1
if count == len(s):
  print('Yes')
else:
  print('No')