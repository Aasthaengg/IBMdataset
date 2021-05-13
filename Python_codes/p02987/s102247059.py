s = input()
s1 = set(s)
if len(s1)==2:
  if s.count(list(s1)[0])==2 and s.count(list(s1)[1])==2: print('Yes')
  else: print('No')
else: print('No')