n, y = map(int, input().split())
tf = False
ans = ""
for i in range(n+1):
  a = y - i * 10000
  for j in range(n-i+1):
    b = a - j * 5000
    tf = True if b == 1000 * (n - i - j) else False
    if tf:
      print('{0} {1} {2}'.format(i, j, n-i-j))
      break
  if tf:
    break
if not(tf):
  print('-1 -1 -1')