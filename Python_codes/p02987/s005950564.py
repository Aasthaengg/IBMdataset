s=list(input())
if len(set(s)) != 2:
  print('No')
elif s.count(s[0]) != 2:
  print('No')
else:
  print('Yes')