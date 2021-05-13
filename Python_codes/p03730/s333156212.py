A, B, C = map(int, input().split())
c = set()
tmp = 0
while 1:
  tmp += A
  if not tmp % B in c:
    c.add(tmp % B)
  else:
    break

print('YES' if C in c else 'NO')