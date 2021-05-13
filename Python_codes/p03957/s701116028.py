s = input()
sc = ''
c = 0

for i in range(len(s)):
  if 'C' == s[i]:
    sc = s[i+1:]
    for j in range(len(sc)):
      if 'F' == sc[j]:
        c += 1

if c > 0:
  print('Yes')
else:
  print('No')