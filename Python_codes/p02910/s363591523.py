s = input()
tapflag = True

for p in range(len(s)):
  if p % 2 == 0:
    if s[p] != 'R' and s[p] != 'U' and s[p] != 'D':
      tapflag = False
  if p % 2 == 1:
    if s[p] != 'L' and s[p] != 'U' and s[p] != 'D':
      tapflag = False
      
if tapflag:
  print('Yes')
else:
  print('No')