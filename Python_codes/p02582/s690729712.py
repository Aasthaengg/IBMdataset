a = str(input())

if a[0] == 'R' and a[1] == 'R' and a[2] == 'R':
  print(3)
elif a[1] == 'R' and a[2] == 'R' and a[0] != 'R':
  print(2)
elif a[0] == 'R' and a[1] == 'R' and a[2] != 'R':
  print(2)
elif 'R' not in a:
  print(0)
else:
  print(1)