a, b = map(int, input().split())
a -= 1
b -= 1
print(82, 51)
for i in range(41):
  for j in range(51):
    if i % 2 == 0 or j % 2 == 0 or b == 0:
      print('.', end='')
    else:
      print('#', end='')
      b -= 1
  print('')
for i in range(41):
  for j in range(51):
    if i % 2 == 0 or j % 2 == 0 or a == 0:
      print('#', end='')
    else:
      print('.', end='')
      a -= 1
  print('')
