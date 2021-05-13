s = input()

a = -1
c = -1
lower = 0
for i in range(len(s)):
  if s[i] == 'A':
    a = i
  if s[i] == 'C':
    c = i
  if 'a' <= s[i] <= 'z':
    lower += 1

if a == 0 and 2 <= c <= len(s) - 2 and lower == len(s) - 2:
  print('AC')
else:
  print('WA')
