A = input()
count = 0
for i in A:
  if i == 'o':
    count += 1
b = len(A) - count
if 15 - b > 7:
  print('YES')
else:
  print('NO')