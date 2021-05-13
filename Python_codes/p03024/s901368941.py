s = raw_input()
c = 0
for ch in s:
  if ch == 'x':
    c += 1
if c <= 7:
  print 'YES'
else:
  print 'NO'