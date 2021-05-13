s = input()
a = 'keyence'
n = len(s)
d =0
for i in range(n):
  for j in range(i,n+1):
    if s[:i]+s[j:] == a:
      d += 1
if d == 0:
  print('NO')
else:
  print('YES')