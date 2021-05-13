cnt = 0
s = input()
for x in s:
  if x == 'x': cnt += 1
print('YES' if cnt < 8 else 'NO')