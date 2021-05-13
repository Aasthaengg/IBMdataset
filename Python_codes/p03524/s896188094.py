s = input()
x = len(s)
a = s.count('a')
b = s.count('b')
c = s.count('c')

if x % 3 == 0:
  if a == b == c:
    print('YES')
  else:
    print('NO')
elif x % 3 == 1:
  if a == b + 1 == c + 1 or b == a + 1 == c + 1 or c == a + 1 == b + 1:
    print('YES')
  else:
    print('NO')
else:
  if a == b == c + 1 or b == c == a + 1 or c == a == b + 1:
    print('YES')
  else:
    print('NO')