n = input()
l = len(n)
k = n.count('o')
if 15-l+k >= 8:
  print('YES')
else:
  print('NO')