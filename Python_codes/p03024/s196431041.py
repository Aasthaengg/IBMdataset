nyuuryoku=input()
a=list(nyuuryoku)
win=a.count('o')
lose=a.count('x')
day=len(a)
if (15-day)+win>=8:
  print('YES')
else:
  print('NO')