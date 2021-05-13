line1 = input()
line2 = input()

new_line2 = line2[::-1]

if line1 == new_line2:
  print('YES')
else:
  print('NO')