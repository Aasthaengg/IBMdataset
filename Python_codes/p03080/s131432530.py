n = int(input())
s = str(input())

r = 0
for i in range(len(s)):
  if s[i] == 'R':
    r += 1

if r > (n-r):
  print('Yes')
else:
  print('No')