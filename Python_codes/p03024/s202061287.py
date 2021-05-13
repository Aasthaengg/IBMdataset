import sys
s = sys.stdin.readline().rstrip()
if len([y for y in s if y == 'x']) >= 8:
  print('NO')
else:
  print('YES')