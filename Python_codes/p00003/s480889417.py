n = int(input())
while n>0:
  l = [int(i) for i in input().split()]
  l.sort()
  if l[0]**2 + l[1] ** 2 == l[2] ** 2:
    print('YES')
  else:
    print('NO')
  n -= 1