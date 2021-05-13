s = input().split()
b = list(s[0][0] + s[0][1] + s[0][2] + s[0][3])
sset = set(b)
if len(sset) == 2:
  print('Yes')
else:
  print('No')