s = input()
a = s.lower()
l = len(s)
c = 0
n = 0

if s[0] == 'A':
  for i in range(2 , l-1):
    if s[i] == 'C':
      c += 1
  if c == 1:
    for i in range(1,l):
      if s[i] != a[i]:
        n += 1
    if n == 1:
      print('AC')
      exit()
print('WA')