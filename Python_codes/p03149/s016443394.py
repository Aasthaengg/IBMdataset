n = list(map(int, input().split()))
n.sort()
t = ''
for i in range(4):
  t += str(n[i])

if t == '1479':
  print('YES')
else:
  print('NO')